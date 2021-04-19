__description__ = 'I/O handling functions for LC Gromacs MD Simulations'


import getopt
import sys


# Parse command-line options
def cmd_parse(usage, coordinate_file=None, slab_file=None, output_file=None, topol_file=None):
    # Check if arguments were provided
    argv = sys.argv[1:]
    if len(argv) < 1:
        print('No command-line arguments specified, exiting...')
        print('Usage:\n' + usage)
        sys.exit(2)

    # Define short option flags
    opts, args = getopt.getopt(argv, 'f:o:p:s:h')

    # Find arguments from options
    for opt, arg in opts:
        if opt in ['-f']:
            coordinate_file = arg
        elif opt in ['-o']:
            output_file = arg
        elif opt in ['-p']:
            topol_file = arg
        elif opt in ['-s']:
            slab_file = arg
        elif opt in ['-h']:
            print(usage)
            sys.exit(1)

    # Handle exceptions and check for valid files
    if coordinate_file is None:
        print('No coordinate file specified, exiting...')
        sys.exit(2)

    if output_file is None:
        print('No output file specified, using default name:')
        print('output.gro')
        output_file = 'output.gro'

    if slab_file is None:
        print('No slab file specified, will not update slab.')

    if topol_file is None:
        print('No topology file specified, will not update topology.')

    # Return values
    return coordinate_file, output_file, topol_file, slab_file


# Open file function
def file_open(file):
    # Read file by iterating through line
    with open(file) as f:
        config = [line.rstrip() for line in f]

    return config


# Parse GRO file format into individual lists
def gro_parse(gro_file):
    # Pull header and footer information
    title, num_atoms, box_size = gro_file[0], gro_file[1], gro_file[-1]

    resid, resname, atomname, atomnum, x_c, y_c, z_c, x_v, y_v, z_v = [], [], [], [], [], [], [], [], [], []

    # Extract GRO file elements
    for i in gro_file:
        if i == title or i == num_atoms or i == box_size:
            pass
        else:
            resid.append(i[0:5].rstrip())
            resname.append(i[5:10].rstrip())
            atomname.append(i[10:15].rstrip())
            atomnum.append(i[15:20].rstrip())
            x_c.append(i[20:28].strip())
            y_c.append(i[28:36].strip())
            z_c.append(i[36:44].strip())
            x_v.append(i[44:52].strip())
            y_v.append(i[52:60].strip())
            z_v.append(i[60:68].strip())
    return title, num_atoms, box_size, resid, resname, atomname, atomnum, x_c, y_c, z_c, x_v, y_v, z_v


# Create gro file list
def gro_stitch(title, num_atoms, box_size, resid, resname, atomname, atomnum, x_c, y_c, z_c, x_v=None, y_v=None,
               z_v=None):
    gro_file = []

    # Find length of file
    file_length = len(resid)

    # Conditional creation logic
    if x_v is None or y_v is None or z_v is None:
        for i in range(file_length):
            gro_file.append(resid[i].rjust(5) + resname[i].rjust(5) + atomname[i].rjust(5) + atomnum[i].rjust(5) +
                            x_c[i].rjust(8) + y_c[i].rjust(8) + z_c[i].rjust(8))
    else:
        for i in range(file_length):
            gro_file.append(resid[i].rjust(5) + resname[i].rjust(5) + atomname[i].rjust(5) + atomnum[i].rjust(5) +
                            x_c[i].rjust(8) + y_c[i].rjust(8) + z_c[i].rjust(8) + x_v[i].rjust(8) + y_v[i].rjust(8) +
                            z_v[i].rjust(8))
    # Add header and footer information
    gro_file.insert(0, num_atoms)
    gro_file.insert(0, title)
    gro_file.append(box_size)

    return gro_file


# Write file function
def file_writer(output_list, output_file):
    with open(output_file, 'w') as f:
        for item in output_list:
            f.write("%s\n" % item)
    print('%s was successfully written!' % output_file)
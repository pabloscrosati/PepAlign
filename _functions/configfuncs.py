__description__ = 'Specific configuration manipulation functions for LC Gromacs MD Simulations'
__version__ = '1.1.2'

# Desolvate configuration file, update topology if specified
def desolvate(config_list):
    desolv_list = []

    # Find solvent atoms and create list excluding these atoms
    for i in config_list:
        resid = i[5:8].strip()
        if resid != 'SOL' and resid != 'ACN':
            desolv_list.append(i)

    # Update atom count in header
    desolv_list[1] = str(len(desolv_list) - 3).rjust(8)

    return desolv_list


# Define box vectors from GRO file
def box_vectors(box_size):
    box_vec = box_size.split()

    return box_vec


# Center chain in box
def center_chain(chain_x_str, chain_y_str, box_x_str, box_y_str):

    # Convert values
    chain_x = [float(i) for i in chain_x_str]
    chain_y = [float(i) for i in chain_y_str]
    box_x = float(box_x_str)
    box_y = float(box_y_str)

    # Find geometric center of chain
    x_cent = sum(chain_x) / len(chain_x)
    y_cent = sum(chain_y) / len(chain_y)

    # Find center of box
    box_x_c = box_x / 2
    box_y_c = box_y / 2

    # Translation vector for chain
    trans_x = box_x_c - x_cent
    trans_y = box_y_c - y_cent

    new_x = []
    new_y = []

    for i in chain_x:
        new_x.append('%.3f' % (i + trans_x))
    for i in chain_y:
        new_y.append('%.3f' % (i + trans_y))

    return new_x, new_y


# Find minimum and maximum value from list
def min_max(coordinates):
    new_list = [float(i) for i in coordinates]
    min_val = min(new_list)
    max_val = max(new_list)
    return float(min_val), float(max_val)


# Modify z-coordinates to minimum position from box bottom
def dropdown(z_coord, min_coord):
    new_z = []
    pull_dist = min_coord - 0.3
    for i in z_coord:
        new_z.append('%.3f' % (float(i) - pull_dist))
    return new_z


# Move coordinates up along z-axis
def target_max(coordinates, max_height, offset):
    # Convert coordinates to float
    converted = [float(i) for i in coordinates]

    # Find max height of specified coordinate
    z_max = max(converted)

    # Algebra for finding translation vector
    target = float(max_height) - offset
    difference = target - z_max
    new_list = []

    # Modify list
    for i in converted:
        new_list.append('%.3f' % (i + difference))

    return new_list


# Removes solvent that is out of the defined space (in z-axis)
def box_trim(target_max, resid, resname, atomname, atomnum, x_c, y_c, z_c, x_v, y_v, z_v, final_list=[]):

    # Variables to track included solvent and rejection state
    SOL_count = 0
    ACN_count = 0
    ok_flag = 1

    # Main function loop to scan all residues for solvent
    for i in range(len(resid)):

        # Logic to search for waters
        # This logic assumes standard GROMACS 3-point water naming
        if atomname[i] == 'OW':
            if float(z_c[i]) < float(target_max):
                ok_flag = 0
            else:
                ok_flag = 1
        elif atomname[i] == 'HW1':
            if float(z_c[i]) < float(target_max) and ok_flag == 0:
                ok_flag = 0
            else:
                ok_flag = 1

        # Write valid water atoms to final list
        elif atomname[i] == 'HW2':
            if float(z_c[i]) < float(target_max) and ok_flag == 0:
                final_list.append(resid[i - 2].rjust(5) + resname[i - 2].rjust(5) + atomname[i - 2].rjust(5) +
                                  atomnum[i - 2].rjust(5) + x_c[i - 2].rjust(8) + y_c[i - 2].rjust(8) +
                                  z_c[i - 2].rjust(8) + x_v[i - 2].rjust(8) + y_v[i - 2].rjust(8) + z_v[i - 2].rjust(8))
                final_list.append(resid[i - 1].rjust(5) + resname[i - 1].rjust(5) + atomname[i - 1].rjust(5) +
                                  atomnum[i - 1].rjust(5) + x_c[i - 1].rjust(8) + y_c[i - 1].rjust(8) +
                                  z_c[i - 1].rjust(8) + x_v[i - 1].rjust(8) + y_v[i - 1].rjust(8) + z_v[i - 1].rjust(8))
                final_list.append(resid[i].rjust(5) + resname[i].rjust(5) + atomname[i].rjust(5) + atomnum[i].rjust(5) +
                                  x_c[i].rjust(8) + y_c[i].rjust(8) + z_c[i].rjust(8) + x_v[i].rjust(8) +
                                  y_v[i].rjust(8) + z_v[i].rjust(8))
                SOL_count += 1
                ok_flag = 1
            else:
                ok_flag = 1

        # Logic to search for acetonitrile atoms
        elif atomname[i] == 'C1' and resname[i] == 'ACN':
            if float(z_c[i]) < float(target_max):
                ok_flag = 0
            else:
                ok_flag = 1
        elif atomname[i] == 'H11' and resname[i] == 'ACN':
            if float(z_c[i]) < float(target_max) and ok_flag == 0:
                ok_flag = 0
            else:
                ok_flag = 1
        elif atomname[i] == 'H12' and resname[i] == 'ACN':
            if float(z_c[i]) < float(target_max) and ok_flag == 0:
                ok_flag = 0
            else:
                ok_flag = 1
        elif atomname[i] == 'H13' and resname[i] == 'ACN':
            if float(z_c[i]) < float(target_max) and ok_flag == 0:
                ok_flag = 0
            else:
                ok_flag = 1
        elif atomname[i] == 'C2' and resname[i] == 'ACN':
            if float(z_c[i]) < float(target_max) and ok_flag == 0:
                ok_flag = 0
            else:
                ok_flag = 1

        # Write valid acetonitrile molecules to final list
        elif atomname[i] == 'N3' and resname[i] == 'ACN':
            if float(z_c[i]) < float(target_max) and ok_flag == 0:
                final_list.append(resid[i - 5].rjust(5) + resname[i - 5].rjust(5) + atomname[i - 5].rjust(5) +
                                  atomnum[i - 5].rjust(5) + x_c[i - 5].rjust(8) + y_c[i - 5].rjust(8) +
                                  z_c[i - 5].rjust(8) + x_v[i - 5].rjust(8) + y_v[i - 5].rjust(8) + z_v[i - 5].rjust(8))
                final_list.append(resid[i - 4].rjust(5) + resname[i - 4].rjust(5) + atomname[i - 4].rjust(5) +
                                  atomnum[i - 4].rjust(5) + x_c[i - 4].rjust(8) + y_c[i - 4].rjust(8) +
                                  z_c[i - 4].rjust(8) + x_v[i - 4].rjust(8) + y_v[i - 4].rjust(8) + z_v[i - 4].rjust(8))
                final_list.append(resid[i - 3].rjust(5) + resname[i - 3].rjust(5) + atomname[i - 3].rjust(5) +
                                  atomnum[i - 3].rjust(5) + x_c[i - 3].rjust(8) + y_c[i - 3].rjust(8) +
                                  z_c[i - 3].rjust(8) + x_v[i - 3].rjust(8) + y_v[i - 3].rjust(8) + z_v[i - 3].rjust(8))
                final_list.append(resid[i - 2].rjust(5) + resname[i - 2].rjust(5) + atomname[i - 2].rjust(5) +
                                  atomnum[i - 2].rjust(5) + x_c[i - 2].rjust(8) + y_c[i - 2].rjust(8) +
                                  z_c[i - 2].rjust(8) + x_v[i - 2].rjust(8) + y_v[i - 2].rjust(8) + z_v[i - 2].rjust(8))
                final_list.append(resid[i - 1].rjust(5) + resname[i - 1].rjust(5) + atomname[i - 1].rjust(5) +
                                  atomnum[i - 1].rjust(5) + x_c[i - 1].rjust(8) + y_c[i - 1].rjust(8) +
                                  z_c[i - 1].rjust(8) + x_v[i - 1].rjust(8) + y_v[i - 1].rjust(8) + z_v[i - 1].rjust(8))
                final_list.append(resid[i].rjust(5) + resname[i].rjust(5) + atomname[i].rjust(5) + atomnum[i].rjust(5) +
                                  x_c[i].rjust(8) + y_c[i].rjust(8) + z_c[i].rjust(8) + x_v[i].rjust(8) +
                                  y_v[i].rjust(8) + z_v[i].rjust(8))
                ACN_count += 1
                ok_flag = 1
            else:
                ok_flag = 1

        # Write all other atoms to list
        else:
            final_list.append(resid[i].rjust(5) + resname[i].rjust(5) + atomname[i].rjust(5) + atomnum[i].rjust(5) +
                              x_c[i].rjust(8) + y_c[i].rjust(8) + z_c[i].rjust(8) + x_v[i].rjust(8) +
                              y_v[i].rjust(8) + z_v[i].rjust(8))

    # Returns final configuration list, counters for included solvent, and list size
    return final_list, SOL_count, ACN_count, len(final_list)

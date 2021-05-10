__program__ = 'Peptide Aligner for Umbrella LC Simulations'
__version__ = '1.1.2'
__title__ = __program__ + ' v' + __version__
__author__ = 'Pablo Scrosati'
__usage__ = 'eqAlign.py -f [*coordinate file, .gro] -s [*slab file, .gro] -o [output file, .gro] -m [*module, 1 or 2]'

# Custom function set
import sys

import _functions as fcc

if __name__ == '__main__':

    print(__title__)
    print('Author: ' + __author__)

    # Pull command-line arguments
    cmd_input = fcc.cmd_parse(__usage__)

    # Module 1
    if cmd_input[4] == '1':
        # Require slab configuration
        if cmd_input[3] is None:
            print('Slab coordinate file not specified, exiting...')
            sys.exit(2)

        if cmd_input[2] is not None:
            print('Topology file specified. It is not used in this module.')
            print('%s will be ignored.' % cmd_input[2])

        # Open and desolvate coordinate files
        peptide_config = fcc.gro_parse(fcc.desolvate(fcc.file_open(cmd_input[0])))
        slab_config = fcc.gro_parse(fcc.desolvate(fcc.file_open(cmd_input[3])))

        # Align and center peptide at top of box using slab vectors
        new_peptide_z = fcc.target_max(peptide_config[9], (slab_config[2].split()[2]), 0.3)
        new_peptide_xy = fcc.center_chain(peptide_config[7], peptide_config[8], (slab_config[2].split()[0]),
                                          (slab_config[2].split()[1]))

        # Find peptide minimum for and align slab
        pep_minmax = fcc.min_max(new_peptide_z)
        new_slab_z = fcc.target_max(slab_config[9], pep_minmax[0], 0.2)

        # Stitch file components together
        final_peptide_config = fcc.gro_stitch(peptide_config[0], peptide_config[1], peptide_config[2],
                                              peptide_config[3], peptide_config[4], peptide_config[5],
                                              peptide_config[6], new_peptide_xy[0], new_peptide_xy[1],
                                              new_peptide_z)
        final_slab_config = fcc.gro_stitch(slab_config[0], slab_config[1], slab_config[2],
                                              slab_config[3], slab_config[4], slab_config[5],
                                              slab_config[6], slab_config[7], slab_config[8],
                                              new_slab_z)

        # Merge configuration files
        final_configuration = fcc.merge_lists(final_peptide_config, final_slab_config, 2)

        # Write output file
        fcc.file_writer(final_configuration, cmd_input[1])

    # Module 2
    elif cmd_input[4] == '2':

        if cmd_input[2] is not None:
            print('Topology file specified. It is not used in this module.')
            print('%s will be ignored.' % cmd_input[2])

        if cmd_input[3] is not None:
            print('Slab file specified. It is not used in this module.')
            print('%s will be ignored.' % cmd_input[3])

        # Open configuration and desolvate
        configuration = fcc.gro_parse(fcc.desolvate(fcc.file_open(cmd_input[0])))

        # Find and adjust coordinates to minimum position
        config_minmax = fcc.min_max(configuration[9])
        new_config_z = fcc.dropdown(configuration[9], config_minmax[0])

        # Create final configuration list
        stitch_configuration = fcc.gro_stitch(configuration[0], configuration[1], configuration[2], configuration[3],
                                             configuration[4], configuration[5], configuration[6], configuration[7],
                                             configuration[8], new_config_z)
        final_configuration = fcc.atm_count(stitch_configuration)

        # Write output file
        fcc.file_writer(final_configuration, cmd_input[1])

    else:
        print('No valid module selected, exiting...')
        sys.exit(3)

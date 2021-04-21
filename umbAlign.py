__program__ = 'Peptide Aligner for Umbrella LC Simulations'
__version__ = '1.1'
__title__ = __program__ + ' v' + __version__
__author__ = 'Pablo Scrosati'
__usage__ = 'eqAlign.py -f [*coordinate file, .gro] -s [*slab file, .gro] -o [output file, .gro]'

# Custom function set
import sys

import _functions as fcc

if __name__ == '__main__':

    print(__title__)
    print('Author: ' + __author__)

    # Pull command-line arguments
    cmd_input = fcc.cmd_parse(__usage__)

    # Require slab configuration
    if cmd_input[3] is None:
        print('Slab coordinate file not specified, exiting...')
        sys.exit(2)

    # Open and desolvate coordinate files
    peptide_confg = fcc.gro_parse(fcc.desolvate(fcc.file_open(cmd_input[0])))
    slab_confg = fcc.gro_parse(fcc.desolvate(fcc.file_open(cmd_input[3])))

    # Align and center peptide at top of box using slab vectors
    new_peptide_z = fcc.target_max(peptide_confg[9], (slab_confg[2].split()[2]), 0.3)
    new_peptide_xy = fcc.center_chain(peptide_confg[7], peptide_confg[8], (slab_confg[2].split()[0]),
                                      (slab_confg[2].split()[1]))

    # Find peptide minimum for and align slab
    pep_minmax = fcc.min_max(new_peptide_z)
    new_slab_z = fcc.target_max(slab_confg[9], pep_minmax[0], 0.2)

    # Stitch file components together
    final_peptide_config = fcc.gro_stitch(peptide_confg[0], peptide_confg[1], peptide_confg[2],
                                          peptide_confg[3], peptide_confg[4], peptide_confg[5],
                                          peptide_confg[6], new_peptide_xy[0], new_peptide_xy[1],
                                          new_peptide_z)
    final_slab_config = fcc.gro_stitch(slab_confg[0], slab_confg[1], slab_confg[2],
                                          slab_confg[3], slab_confg[4], slab_confg[5],
                                          slab_confg[6], slab_confg[7], slab_confg[8],
                                          new_slab_z)

    # Merge configuration files
    final_configuration = fcc.merge_lists(final_peptide_config, final_slab_config, 2)

    # Write output file
    fcc.file_writer(final_configuration, cmd_input[1])

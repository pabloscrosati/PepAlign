__program__ = 'Peptide Aligner for Umbrella LC Simulations'
__version__ = '1.1'
__title__ = __program__ + ' v' + __version__
__author__ = 'Pablo Scrosati'
__usage__ = 'eqAlign.py -f [*coordinate file, .gro] -s [*slab file, .gro] -o [output file, .gro] -p [topology file, ' \
            '.top] '

# Custom function set
import sys

import _functions as fcc

if __name__ == '__main__':

    print(__title__)
    print('Author: ' + __author__)

    # Pull command-line arguments
    cmd_input = fcc.cmd_parse(__usage__)

    if cmd_input[3] is None:
        print('Slab coordinate file not specified, exiting...')
        sys.exit(2)

    # Obtain and parse configuration file
    peptide_configuration = fcc.gro_parse(fcc.file_open(cmd_input[0]))
    slab_configuration = fcc.gro_parse(fcc.file_open(cmd_input[3]))

    # Align peptide at top of box using slab vectors

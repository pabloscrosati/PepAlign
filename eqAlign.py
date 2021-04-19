__program__ = 'Peptide Aligner for Equilibrium LC Simulations'
__version__ = 'development'
__title__ = __program__ + ' v' + __version__
__author__ = 'Pablo Scrosati'
__usage__ = 'eqAlign.py -f [*coordinate file, .gro] -s [slab file, .gro] -o [output file, .gro] -p [topology file, ' \
            '.top] '

import _functions as fcc

print(__title__)
print('Author: ' + __author__)

fcc.cmd_parse(__usage__)

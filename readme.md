# Peptide Aligner for LC MD Gromacs Simulations
**Version 1.1, Written by: Pablo Scrosati**

## Umbrella Sampling Configurations
Usage:`python umbAlign.py -f [peptide.gro] -s [slab.gro] -o [output.gro] -m [module, 1 or 2]`
#### To Do
* Add command-line interpretation for determining module

### Initial Burial (Module 1)
#### Current Functionality
* Remove solvent from input configurations
* Align peptide to top of definable configuration box
* Align LC slab to definable position below peptide
* Writes output configuration file in .gro format
#### To Do
* Add topology modification support
    * Topology handling exists in I/O handling, missing logic when reading configuration files
    
### Configuration for Defining Reaction Coordinate (Module 2)
#### Current Functionality
* Brings buried peptide and slab configuration to box minimum to define reaction coordinate
* Writes output configuration file in .gro format
#### To Do
* Add topology modification support
    * Topology handling exists in I/O handling, missing logic when reading configuration files
    
## Equilibrium Simulations
Usage:`python eqAlign.py -f [peptide.gro] -s [slab.gro] -o [output.gro]`
### Program Objectives
* Create reproducible initial conditions for peptide positioning
* Orient peptide at box extreme
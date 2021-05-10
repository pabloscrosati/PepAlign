# Peptide Aligner for LC MD Gromacs Simulations
**Version 1.1.1, Written by: Pablo Scrosati**

See changelog.md for updates.

Items in listed as "To Do" are essential features that are planned. Ideas may be implemented on a need basis.

## Umbrella Sampling Configurations
Usage: `python umbAlign.py -f [peptide.gro] -s [slab.gro] -o [output.gro] -m [module, 1 or 2]`
#### To Do
* Topology handling logic

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
Usage: `python eqAlign.py -f [peptide.gro] -s [slab.gro] -o [output.gro]`
#### Current Functionality
* Aligns and centers peptide in slab box at top of box
* Writes output configuration in .gro format
#### To Do
* Add topology modification support
    * Topology handling exists in I/O handling, missing logic when reading configuration files
  
## Additional Modules
These modules are in development, or are included in the main build as a pre-release script.
Proper documentation will be provided upon completion and integration with the primary functions.
### Desolvator
* Removes solvent in unrealistic locations
### BoxAdjuster
* Name may change
* Adjust box dimensions based on solvent composition to preserve pore size

**Known Bugs**
* Does not account or correct for 50/50 solvent mixtures
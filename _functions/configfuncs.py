__description__ = 'Specific configuration manipulation functions for LC Gromacs MD Simulations'


def desolvate(config_list, topology=None):
    desolv_list = []

    # Find solvent atoms and create list excluding these atoms
    for i in config_list:
        resid = i[5:8].strip()
        if resid != 'SOL' and resid != 'ACN':
            desolv_list.append(i)
    # Update atom count in header
    desolv_list[1] = str(len(desolv_list) - 3).rjust(8)

    if topology is not None:
        topol = []
        with open(topology) as f:
            lines = [line.rstrip() for line in f]
        for i in lines:
            resid = i[0:3].strip()
            if resid != 'SOL' and resid != 'ACN':
                topol.append(i)

    return desolv_list, topol

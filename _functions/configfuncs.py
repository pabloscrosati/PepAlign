__description__ = 'Specific configuration manipulation functions for LC Gromacs MD Simulations, v1.1'


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

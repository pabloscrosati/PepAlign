__program__ = 'Box Height Adjuster'
__version__ = '0.2'
__title__ = __program__ + ' v' + __version__
__author__ = 'Pablo Scrosati'
__usage__ = 'boxAdjuster.py -f [*coordinate file, .gro] -p [topology file, .top] -o [output file, .gro]'

import _functions as fcc

def box_trim(target_max, resid, resname, atomname, atomnum, x_c, y_c, z_c, x_v, y_v, z_v):
    final_list = []
    SOL_count = 0
    ACN_count = 0
    ok_flag = 1
    for i in range(len(resid)):
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
        else:
            final_list.append(resid[i].rjust(5) + resname[i].rjust(5) + atomname[i].rjust(5) + atomnum[i].rjust(5) +
                              x_c[i].rjust(8) + y_c[i].rjust(8) + z_c[i].rjust(8) + x_v[i].rjust(8) +
                              y_v[i].rjust(8) + z_v[i].rjust(8))
    return final_list, SOL_count, ACN_count, len(final_list)

topol_list = []

if __name__ == '__main__':

    print(__title__)
    print('Author: ' + __author__)

    cmd_input = fcc.cmd_parse(__usage__)

    config = fcc.gro_parse(fcc.file_open(cmd_input[0]))

    updated_config = box_trim(11.7, config[3], config[4], config[5], config[6], config[7], config[8], config[9],
                              config[10], config[11], config[12])

    final_list = updated_config[0]
    final_list.insert(0, str(updated_config[3]).rjust(8))
    final_list.insert(0, config[0].rjust(8))
    final_list.append(config[2])

    with open(cmd_input[1], 'w') as f:
        for item in final_list:
            f.write("%s\n" % item)

    if cmd_input[2] is not None:
        print('Topology file provided, will update.')
        with open(cmd_input[2]) as topol:
            lines = [line.rstrip() for line in topol]
        for i in lines:
            resname = i[0:4].strip()
            if resname == 'SOL':
                topol_list.append('SOL' + str(updated_config[1]).rjust(17))
            elif resname == 'ACN':
                topol_list.append('ACN' + str(updated_config[2]).rjust(17))
            else:
                topol_list.append(i)
        # Write backup file
        with open(cmd_input[2] + '.backup', 'w') as f:
            for item in lines:
                f.write("%s\n" % item)
        with open(cmd_input[2], 'w') as f:
            for item in topol_list:
                f.write("%s\n" % item)
    else:
        print('No topology file specified, update manually.')
        print('Water (SOL) molecules present:', updated_config[1])
        print('Acetonitrile (ACN) molecules present:', updated_config[2])

    print('Process completed successfully!')

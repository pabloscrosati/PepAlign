__program__ = 'Box Height Adjuster'
__version__ = '0.2'
__title__ = __program__ + ' v' + __version__
__author__ = 'Pablo Scrosati'
__usage__ = 'boxAdjuster.py -f [*coordinate file, .gro] -p [topology file, .top] -o [output file, .gro]'

import _functions as fcc

if __name__ == '__main__':

    print(__title__)
    print('Author: ' + __author__)

    topol_list=[]

    cmd_input = fcc.cmd_parse(__usage__)

    config = fcc.gro_parse(fcc.file_open(cmd_input[0]))

    updated_config = fcc.box_trim(11.7, config[3], config[4], config[5], config[6], config[7], config[8], config[9],
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
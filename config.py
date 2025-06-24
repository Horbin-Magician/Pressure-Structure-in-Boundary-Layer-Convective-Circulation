import os

OUTPUT_ROOT_PATH = './output/'
PALM_DATA_ROOT_PATHS = ['./data/']

colors = ['#1F77B4', 'orange', 'g', 'r', 'purple', 'brown', # 蓝色 橙色 绿色 红色 紫色 棕色
          '#E377C2', '#7F7F7F', '#17BECF', '#BCBD22', '#FF9896', # 粉色 灰色 青色 黄色绿 浅红色
          '#C5B0D5', '#98DF8A', '#FFBB78', '#AEC7E8', 'black', 'white'] # 浅紫色 浅绿色 浅橙色 浅蓝色 黑色 白色

line_styles = ['-', '--', ':', '-.', '-o', '-x', '-^', '-v']

default_variable_configs = {
    'w': {
        'unit':'m/s',
        'z_coords':'zw_3d',
        'x_coords':'x',
        'y_coords':'y',
        'levels':[-3.0, -2.0, -1.0, 0, 1.0, 2.0, 3.0]
    },
    'u': {
        'unit':'m/s',
        'z_coords':'zu_3d',
        'x_coords':'xu',
        'y_coords':'y',
        'levels':[-3.0, -2.0, -1.0, 0, 1.0, 2.0, 3.0]
    },
    'theta': {
        'unit':'K',
        'z_coords':'zu_3d',
        'x_coords':'x',
        'y_coords':'y',
        'levels':[-3.0, -2.0, -1.0, 0, 1.0, 2.0, 3.0]
    },
    'p': {
        'unit':'Pa',
        'z_coords':'zu_3d',
        'x_coords':'x',
        'y_coords':'y',
        'levels':[-3.0, -2.0, -1.0, 0, 1.0, 2.0, 3.0]
    },
}

experiments = {
    'U0':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None, 'p': None}
    },
    'U0_Y0.5':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None, 'p': None}
    },
    'U0_Y1.0':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None, 'p': None}
    },
    'U0_CM0.3':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'U0_CM0.5':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'U0_CM1.0':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'U0_G20':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'U0_G100':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'U4':{
        'u': 4,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'U4_CM0.5':{
        'u': 4,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'U0_PR-1':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'U0_PR-2':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'U0_PR+1':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'U0_PR+2':{
        'u': 0,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
    'E-10-10-NN':{
        'u': 10,
        'variables': {'w':None, 'u':None, 'theta':None}
    },
}

def get_experiment_config(flag:str) -> str:
    if flag in experiments.keys():
        return_config = {}
        variables_config = experiments[flag]['variables']
        for variable in experiments[flag]['variables'].keys():
            if variables_config[variable] == None:
                variables_config[variable] = default_variable_configs[variable]
        return_config['variables'] = variables_config
        return_config['flag'] = flag
        return return_config
    else:
        return None

# Return the file name according to related information
def get_file_name(flag:str, type:str = '3d', grid_num:int = 1, file_num:int = None) -> str:
    '''
    get file name according to related information
    :param flag: flag of experiment, 'E-00-10'
    :param type: type of data, '3d', 'av', 'pr', 'ts'
    :param grid_num: grid number, 1 for coarse grid, 2 for fine grid
    :param file_num: file number, None for all files
    :return: file name
    '''
    return_name = f'{flag}_{type}'
    if(grid_num > 1): return_name += f'_N{grid_num:02d}'
    if(file_num == None): return_name += '.*.nc'
    else: return_name += f'.{file_num:03d}.nc'
    return return_name
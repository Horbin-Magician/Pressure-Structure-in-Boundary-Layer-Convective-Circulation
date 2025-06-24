import xarray as xr

import config as cfg


def load_base_data(flag:str, grid_num:int= 1, type:str="3d", file_num:int=None) -> xr.Dataset:
    '''
    Load base data from file
    :param flag: flag of experiment, 'E-00-10'
    :param grid_num: grid number, 1 for coarse grid, 2 for fine grid
    :param type: type of data, '3d', 'av', 'pr', 'ts'
    :param file_num: file number, None for all files
    :return: dataset
    '''
    data_path = './data/' + cfg.get_file_name(flag, type, grid_num, file_num)
    print(f'[info] loader load data: {data_path}')
    dataset = xr.open_mfdataset(data_path)
    return dataset
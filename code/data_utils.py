import pandas as pd
import numpy as np
import os

def add_relative_XY_GNSS(df , cols = ['Lat_GNSS', 'Long_GNSS'], norm_by_first = False , if_print = False ):
    X_Y_list = []
    for lat_long in df[cols].to_numpy():
        X_Y_list.append(np.array(lat_long_to_local_XY(lat_long)))
    X_Y_list = np.array(X_Y_list)
    df[['X_GNSS_km' ,'Y_GNSS_km' ]] = X_Y_list
    df[['X_GNSS_meter' ,'Y_GNSS_meter' ]] = X_Y_list*1000
    if if_print:
        print('Mean of X {} [km] and Y: {} [km]\nMean of X {} [m], and Y {} [m]'.format(
                            X_Y_list[: , 0].mean() , X_Y_list[: , 1].mean(),
                            (X_Y_list[: , 0]*1000).mean() , (X_Y_list[: , 1]*1000).mean()))
    if norm_by_first == True:
        rel_xy =  df[['X_GNSS_km' ,'Y_GNSS_km' ]].to_numpy()[0]
        if if_print:
            print('Creating Relative accourding to first measurment is: {} [km]'.format(rel_xy))
    if if_print:
        print('rel XY mean: {} [km] , in meters: {} [m]'.format(rel_xy , (rel_xy*1000)))
    df[['rel_X_GNSS_km' ,'rel_Y_GNSS_km' ]] = df[['X_GNSS_km' ,'Y_GNSS_km' ]] - rel_xy
    df[['rel_X_GNSS_meter' ,'rel_Y_GNSS_meter' ]] = df[['X_GNSS_meter' ,'Y_GNSS_meter' ]] - rel_xy*1000
    return df

def lat_long_to_local_XY(lat_long):
    lat_deg = lat_long[0]
    long_deg = lat_long[1]
    R_e = 6378 # km
    lat_rad = np.radians(lat_deg)
    long_rad = np.radians(long_deg)
    X = R_e * lat_rad
#     X = R_e * lat_deg
#     Y = R_e * np.cos(lat_rad)
    Y = R_e * np.cos(long_rad)
    return X , Y

def import_dots_from_pos_subfolders(pos_subfolders , dots_conf_path):
    dots_filnames_list = []
    dots_df_list = []
    for sub_i , sub_name in enumerate(pos_subfolders):
        sub_path = os.path.join(dots_conf_path , sub_name)
        dots_names = [d_name for d_name in os.listdir(sub_path) if '.csv' in d_name]
        dots_filnames_list.extend(dots_names)
        dots_dfs = [pd.read_csv(os.path.join(sub_path , d_name)) for d_name in dots_names]
        dots_df_list.extend(dots_dfs)
    return dots_filnames_list , dots_df_list


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_trajectories_reconstruction_rtk(file_names_list , pd_list , name_prefix = 'MRU measurs' , platform = 'Car_Exp', conf_name = 'Conf_1'):
    for f_i , f_name in enumerate(file_names_list):
        if len(name_prefix) >= 1:
            name_temp = f_name[len(name_prefix) + 1:f_name.find('.csv')]
        else:
            name_temp = f_name

        scatter_plot_XY_of_MRU(pd_list[f_i] , cols = ['rel_X_GNSS_meter', 'rel_Y_GNSS_meter'],
                               title = '{} {} Trajectory {}\nGNSS-RTK relative XY reconstruction'.format(platform,conf_name,name_temp))

def scatter_plot_XY_of_MRU(df , cols = [ 'X_GNSS_km' ,'Y_GNSS_km'] , title ='Scatter Plot of XY in km'):
    xy_to_scatter = df[cols].to_numpy()
    plt.figure(figsize = ( 10,10))
    plt.title(title)
    plt.scatter(xy_to_scatter[0, 0], xy_to_scatter[0, 1], label='Start XY', marker= 'P',s = 200 , color = 'green')
    plt.scatter(xy_to_scatter[1:-1 , 0] , xy_to_scatter[1:-1 , 1] , label = 'Traj. XY')
    plt.scatter(xy_to_scatter[-1, 0], xy_to_scatter[-1, 1], label='Last XY' , marker= 'X' , color = 'red' )
    plt.xlabel('X [meters]')
    plt.ylabel('Y [meters]')
    plt.grid()
    plt.legend()
    plt.show(block = False)
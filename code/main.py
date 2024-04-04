
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from tabulate import tabulate
import os
import EDA_utils
import data_utils


if __name__ == '__main__':
    root_data_path = '..\\Data'
    platforms_folders = ["Car_Exp", "ROSBOT_Exp"]
    confs_folders = ["Conf_1", "Conf_2", "Conf_3"]
    dots_and_mru_folder = ["MRU", 'DOTs']
    conf_sub_folders = [["Ceiling" , "Top" , "Bottom"] if c_fold == "Conf_1" else ["Top" , "Bottom"] for c_fold in confs_folders]

    # Import data and visualize it

    for platform_i , platform_fold in enumerate(platforms_folders):
        platform_path = os.path.join(root_data_path, platform_fold)
        for conf_i, conf_folder in enumerate(confs_folders):
            conf_path = os.path.join(platform_path , conf_folder)
            exp_mru_path = os.path.join(conf_path ,dots_and_mru_folder[0] )
            exp_dots_path = os.path.join(conf_path ,dots_and_mru_folder[1] )

            # Import DOTS files names from all positions on configuration
            dots_pos_subfolders_to_import = conf_sub_folders[conf_i]
            dots_filename_list , dots_df_list = data_utils.import_dots_from_pos_subfolders(dots_pos_subfolders_to_import , exp_dots_path)

            # Import MRU files and add approximation of XY from Lat,long to plot in meters
            mru_file_names_list = [f for f in os.listdir(exp_mru_path) if '.csv' in f]
            mru_df_list = [pd.read_csv(os.path.join(exp_mru_path,f)) for f in mru_file_names_list]
            mru_data_df_list_with_rel_XY = [
                data_utils.add_relative_XY_GNSS(mru_df, cols=['Lat_GNSS', 'Long_GNSS'], norm_by_first=True,
                                         if_print=False) for mru_df in mru_df_list]
            trajectory_names_from_mru = [t_name[len('MRU measurs') +1 : t_name.find('.csv')] for t_name in mru_file_names_list]

            # Plot trajectories reconstruction
            EDA_utils.plot_trajectories_reconstruction_rtk(trajectory_names_from_mru, mru_data_df_list_with_rel_XY,
                                                           name_prefix=''
                                                           , platform=platform_fold, conf_name=conf_folder)

    print('--------------------------------------------- Finished Producting all RTK Reconstruction Plots ---------------------------------------------')
    plt.show()
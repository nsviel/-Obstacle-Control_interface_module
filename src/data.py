#! /usr/bin/python
#---------------------------------------------

from param import param_co
from src import io
from scheme import scheme_plot


def process_lidar_1_data(data):
    path = param_co.state_co["path"]["path_l1_file"]
    io.write_lidar_data(path, data)
    scheme_plot.update_plot_l1(len(data))

def process_lidar_2_data(data):
    path = param_co.state_co["path"]["path_l2_file"]
    io.write_lidar_data(path, data)
    scheme_plot.update_plot_l2(len(data))

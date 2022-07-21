#! /usr/bin/python
#---------------------------------------------

from param import param_co
from scheme import scheme_plot


def process_lidar_1_data(data):
    path = param_co.state_py["lidar_1"]["file"]
    write_lidar_data(path, data)
    scheme_plot.update_plot(len(data))

def process_lidar_2_data(data):
    path = param_co.state_py["lidar_2"]["file"]
    write_lidar_data(path, data)
    scheme_plot.update_plot(len(data))

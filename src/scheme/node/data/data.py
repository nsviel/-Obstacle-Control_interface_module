#---------------------------------------------
from src.param import param_interface
from src.misc import io
from src.scheme.node.interface import scheme_plot


def process_l1_data(data):
    path = param_interface.state_interface["path"]["path_l1_file"]
    io.write_lidar_data(path, data)
    scheme_plot.update_plot_l1(len(data))

def process_l2_data(data):
    path = param_interface.state_interface["path"]["path_l2_file"]
    io.write_lidar_data(path, data)
    scheme_plot.update_plot_l2(len(data))

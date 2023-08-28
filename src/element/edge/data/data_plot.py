#---------------------------------------------
from src.utils import function
from src.param import param_control
import dearpygui.dearpygui as dpg
import random


class Data_plot:
    def __init__(self, ID):
        self.ID = ID

    def init_plot(self):
        for i in range(0, param_control.nb_tic):
            param_control.vec_x.append(i)
            param_control.vec_y_l1.append(0)
            param_control.vec_y_l2.append(0)

    def update_plot_l1(data_len):
        param_control.vec_y_l1.pop(0)
        param_control.vec_y_l1.append(data_len)
        dpg.set_value('l1_plot', [param_control.vec_x, param_control.vec_y_l1])

    def update_plot_l2(data_len):
        param_control.vec_y_l2.pop(0)
        param_control.vec_y_l2.append(data_len)
        dpg.set_value('l2_plot', [param_control.vec_x, param_control.vec_y_l2])

    def update_plot_random():
        param_control.vec_y_l1.pop(0)
        param_control.vec_y_l2.pop(0)

        param_control.vec_y_l1.append(random.randint(0, 1248))
        param_control.vec_y_l2.append(random.randint(0, 1248))

        dpg.set_value('l1_plot', [param_control.vec_x, param_control.vec_y_l1])
        dpg.set_value('l2_plot', [param_control.vec_x, param_control.vec_y_l2])

def process_l1_data(data):
    path = param_control.state_control["ssd"]["path"]["path_l1_file"]
    io.write_lidar_data(path, data)
    plot.update_plot_l1(len(data))

def process_l2_data(data):
    path = param_control.state_control["ssd"]["path"]["path_l2_file"]
    io.write_lidar_data(path, data)
    plot.update_plot_l2(len(data))

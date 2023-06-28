#---------------------------------------------
from src.param import param_interface

import dearpygui.dearpygui as dpg

import random


def init_plot():
    for i in range(0, param_interface.nb_tic):
        param_interface.vec_x.append(i)
        param_interface.vec_y_l1.append(0)
        param_interface.vec_y_l2.append(0)

def update_plot_l1(data_len):
    param_interface.vec_y_l1.pop(0)
    param_interface.vec_y_l1.append(data_len)
    dpg.set_value('l1_plot', [param_interface.vec_x, param_interface.vec_y_l1])

def update_plot_l2(data_len):
    param_interface.vec_y_l2.pop(0)
    param_interface.vec_y_l2.append(data_len)
    dpg.set_value('l2_plot', [param_interface.vec_x, param_interface.vec_y_l2])

def update_plot_random():
    param_interface.vec_y_l1.pop(0)
    param_interface.vec_y_l2.pop(0)

    param_interface.vec_y_l1.append(random.randint(0, 1248))
    param_interface.vec_y_l2.append(random.randint(0, 1248))

    dpg.set_value('l1_plot', [param_interface.vec_x, param_interface.vec_y_l1])
    dpg.set_value('l2_plot', [param_interface.vec_x, param_interface.vec_y_l2])

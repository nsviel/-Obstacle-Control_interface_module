#! /usr/bin/python
#---------------------------------------------

from param import param_co

import dearpygui.dearpygui as dpg

import random


def init_plot():
    for i in range(0, param_co.nb_tic):
        param_co.vec_x.append(i)
        param_co.vec_y_l1.append(0)
        param_co.vec_y_l2.append(0)

def update_plot():
    param_co.vec_y_l1.pop(0)
    param_co.vec_y_l2.pop(0)

    param_co.vec_y_l1.append(0)
    param_co.vec_y_l2.append(0)

    dpg.set_value('l1_plot', [param_co.vec_x, param_co.vec_y_l1])
    dpg.set_value('l2_plot', [param_co.vec_x, param_co.vec_y_l2])

def update_plot_random():
    param_co.vec_y_l1.pop(0)
    param_co.vec_y_l2.pop(0)

    param_co.vec_y_l1.append(random.randint(0, 1248))
    param_co.vec_y_l2.append(random.randint(0, 1248))

    dpg.set_value('l1_plot', [param_co.vec_x, param_co.vec_y_l1])
    dpg.set_value('l2_plot', [param_co.vec_x, param_co.vec_y_l2])

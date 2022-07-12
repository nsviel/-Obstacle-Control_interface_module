#! /usr/bin/python
#---------------------------------------------

from param import param_co

import dearpygui.dearpygui as dpg


def loop():
    loop_packet()

def loop_packet():
    dpg.set_value("l1_packet", param_co.state_py["lidar_1"]["nb_packet"])
    dpg.set_value("l2_packet", param_co.state_py["lidar_2"]["nb_packet"])

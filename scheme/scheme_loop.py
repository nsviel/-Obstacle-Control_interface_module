#! /usr/bin/python
#---------------------------------------------

from param import param_co

import dearpygui.dearpygui as dpg


def loop():
    loop_packet()
    loop_bandwidth()

def loop_packet():
    dpg.set_value("l1_packet", param_co.state_py["lidar_1"]["packet"]["value"])
    dpg.set_value("l2_packet", param_co.state_py["lidar_2"]["packet"]["value"])

def loop_bandwidth():
    value = param_co.state_py["lidar_1"]["bandwidth"]["value"]
    min = param_co.state_py["lidar_1"]["bandwidth"]["min"]
    mean = param_co.state_py["lidar_1"]["bandwidth"]["mean"]
    max = param_co.state_py["lidar_1"]["bandwidth"]["max"]
    bandwidth = "%s [%s, %s, %s]"% (value, min, mean, max)
    dpg.set_value("l1_bandwidth", bandwidth)

    value = param_co.state_py["lidar_2"]["bandwidth"]["value"]
    min = param_co.state_py["lidar_2"]["bandwidth"]["min"]
    mean = param_co.state_py["lidar_2"]["bandwidth"]["mean"]
    max = param_co.state_py["lidar_2"]["bandwidth"]["max"]
    bandwidth = "%s [%s, %s, %s]"% (value, min, mean, max)
    dpg.set_value("l2_bandwidth", bandwidth)

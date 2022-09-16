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
    dpg.set_value("l1_bdw_val", param_co.state_py["lidar_1"]["bandwidth"]["value"])
    min = param_co.state_py["lidar_1"]["bandwidth"]["min"]
    mean = param_co.state_py["lidar_1"]["bandwidth"]["mean"]
    max = param_co.state_py["lidar_1"]["bandwidth"]["max"]
    bandwidth = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("l1_bdw_range", bandwidth)

    dpg.set_value("l2_bdw_val", param_co.state_py["lidar_2"]["bandwidth"]["value"])
    min = param_co.state_py["lidar_2"]["bandwidth"]["min"]
    mean = param_co.state_py["lidar_2"]["bandwidth"]["mean"]
    max = param_co.state_py["lidar_2"]["bandwidth"]["max"]
    bandwidth = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("l2_bdw_range", bandwidth)

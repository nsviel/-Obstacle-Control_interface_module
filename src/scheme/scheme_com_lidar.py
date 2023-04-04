#---------------------------------------------
from src.param import param_interface
from src.HTTPS import https_client_get
from src.HTTPS import https_client_post
from src.HTTPS import https_client_con
from src.SOCK import sock_server
from src.misc import saving
from src.misc import wallet

import dearpygui.dearpygui as dpg


# LiDAR motor start
def command_l1_start():
    https_client_post.post_param_value("acquisition", None, "lidar_1", "start")
def command_l2_start():
    https_client_post.post_param_value("acquisition", None, "lidar_2", "start")

# LiDAR motor stop
def command_l1_stop():
    https_client_post.post_param_value("acquisition", None, "lidar_1", "stop")
def command_l2_stop():
    https_client_post.post_param_value("acquisition", None, "lidar_2", "stop")

# LiDAR motor speed
def command_l1_speed():
    l1_speed = dpg.get_value("l1_speed")
    param_interface.state_capture["lidar_1"]["speed"] = l1_speed
    https_client_post.post_param_value("acquisition", "lidar_1", "speed", l1_speed)
def command_l2_speed():
    l2_speed = dpg.get_value("l2_speed")
    param_interface.state_capture["lidar_2"]["speed"] = l2_speed
    https_client_post.post_param_value("acquisition", "lidar_2", "speed", l2_speed)

# LiDAR device
def command_l1_dev():
    l1_dev = dpg.get_value("capture_l1_device")
    https_client_post.post_param_value("acquisition", "lidar_1", "device", l1_dev)
def command_l2_dev():
    l2_dev = dpg.get_value("capture_l2_device")
    https_client_post.post_param_value("acquisition", "lidar_2", "device", l2_dev)

# Misc LiDAR command
def command_combo_lidar_main():
    lidar_main = dpg.get_value("edge_sock_client_l1_combo_lidar_main")
    https_client_post.post_param_value("edge", "self", "lidar_main", lidar_main)
    param_interface.lidar_main = lidar_main

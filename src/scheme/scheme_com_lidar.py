#---------------------------------------------
from src.param import param_co
from src.HTTPS import https_client_get
from src.HTTPS import https_client_post
from src.HTTPS import https_client_con
from src.SOCK import sock_server
from src.misc import saving
from src.misc import wallet

import dearpygui.dearpygui as dpg


# LiDAR motor start
def command_l1_start():
    https_client_post.post_param_value("py", None, "lidar_1", "start")
def command_l2_start():
    https_client_post.post_param_value("py", None, "lidar_2", "start")

# LiDAR motor stop
def command_l1_stop():
    https_client_post.post_param_value("py", None, "lidar_1", "stop")
def command_l2_stop():
    https_client_post.post_param_value("py", None, "lidar_2", "stop")

# LiDAR motor speed
def command_l1_speed():
    l1_speed = dpg.get_value("l1_speed")
    param_co.state_py["lidar_1"]["speed"] = l1_speed
    https_client_post.post_param_value("py", "lidar_1", "speed", l1_speed)
def command_l2_speed():
    l2_speed = dpg.get_value("l2_speed")
    param_co.state_py["lidar_2"]["speed"] = l2_speed
    https_client_post.post_param_value("py", "lidar_2", "speed", l2_speed)

# Misc LiDAR command
def command_combo_lidar_main():
    lidar_main = dpg.get_value("hu_sock_client_l1_combo_lidar_main")
    https_client_post.post_param_value("hu", "self", "lidar_main", lidar_main)
    param_co.lidar_main = lidar_main

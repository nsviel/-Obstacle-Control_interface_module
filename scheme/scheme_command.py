#---------------------------------------------
from param import param_co
from HTTP import http_client_get
from HTTP import http_client_post
from SOCK import sock_server
from src import saving
from src import wallet

import dearpygui.dearpygui as dpg


def command_l1_start():
    print("[\033[1;32mOK\033[0m] LiDAR 1 \033[1;32mstart\033[0m")
    http_client_post.post_param_value("py", None, "lidar_1", "start")

def command_l1_stop():
    print("[\033[1;32mOK\033[0m] LiDAR 1 \033[1;31mstop\033[0m")
    http_client_post.post_param_value("py", None, "lidar_1", "stop")

def command_l2_start():
    print("[\033[1;32mOK\033[0m] LiDAR 2 \033[1;32mstart\033[0m")
    http_client_post.post_param_value("py", None, "lidar_2", "start")

def command_l2_stop():
    print("[\033[1;32mOK\033[0m] LiDAR 2 \033[1;31mstop\033[0m")
    http_client_post.post_param_value("py", None, "lidar_2", "stop")

def command_false_alarm():
    print("[\033[1;32mOK\033[0m] Send false alarm")
    http_client_post.post_param_value("hu", None, "sncf", "false_alarm")

def command_lidar_source():
    source_l1 = dpg.get_value("hu_sock_client_l1_source")
    if(source_l1 == "Lidar 1"):
        source_l1 = "lidar_1"
        source_l2 = "lidar_2"
    else:
        source_l1 = "lidar_2"
        source_l2 = "lidar_1"
    dpg.set_value("hu_sock_client_l2_source", source_l2)
    http_client_post.post_param_value("hu", "self", "sock_server_l1_source", source_l1)
    http_client_post.post_param_value("hu", "self", "sock_server_l2_source", source_l2)

def command_new_save():
    saving.determine_path()

def command_ssd_editing():
    dpg.set_value("ssd_active", False)
    param_co.state_co["ssd"]["activated"] = False
    param_co.state_co["path"]["file_name_add"] = dpg.get_value("ssd_path_add")
    param_co.path_ssd = dpg.get_value("ssd_path")
    saving.determine_path()

def command_comboip():
    hu_ip = wallet.get_ip_from_key(dpg.get_value("hu_wallet"))
    py_ip = wallet.get_ip_from_key(dpg.get_value("py_wallet"))
    ed_ip = wallet.get_ip_from_key(dpg.get_value("ed_wallet"))
    sncf_ip = wallet.get_ip_from_key(dpg.get_value("sncf_wallet"))
    if(hu_ip != None):
        param_co.state_co["hubium"]["ip"] = hu_ip
        dpg.set_value("hu_ip", hu_ip)
    if(py_ip != None):
        param_co.state_hu["pywardium"]["ip"] = py_ip
        dpg.set_value("py_ip", py_ip)
        http_client_post.post_param_value("hu", "pywardium", "ip", py_ip)
    if(ed_ip != None):
        param_co.state_hu["edge"]["ip"] = ed_ip
        dpg.set_value("ed_ip", ed_ip)
        http_client_post.post_param_value("hu", "edge", "ip", ed_ip)
    if(sncf_ip != None):
        param_co.state_hu["sncf"]["broker_ip"] = sncf_ip
        dpg.set_value("sncf_ip", sncf_ip)
        http_client_post.post_param_value("hu", "sncf", "broker_ip", sncf_ip)

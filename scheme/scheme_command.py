#---------------------------------------------
from param import param_co
from HTTPS import https_client_get
from HTTPS import https_client_post
from HTTPS import https_client_con
from SOCK import sock_server
from src import saving
from src import wallet

import dearpygui.dearpygui as dpg


def command_l1_start():
    print("[\033[1;32mOK\033[0m] LiDAR 1 \033[1;32mstart\033[0m")
    https_client_post.post_param_value("py", None, "lidar_1", "start")

def command_l1_stop():
    print("[\033[1;32mOK\033[0m] LiDAR 1 \033[1;31mstop\033[0m")
    https_client_post.post_param_value("py", None, "lidar_1", "stop")

def command_l2_start():
    print("[\033[1;32mOK\033[0m] LiDAR 2 \033[1;32mstart\033[0m")
    https_client_post.post_param_value("py", None, "lidar_2", "start")

def command_l2_stop():
    print("[\033[1;32mOK\033[0m] LiDAR 2 \033[1;31mstop\033[0m")
    https_client_post.post_param_value("py", None, "lidar_2", "stop")

def command_false_alarm():
    print("[\033[1;32mOK\033[0m] Send false alarm")
    https_client_post.post_param_value("hu", None, "sncf", "false_alarm")

def command_lidar_source():
    lidar_main = dpg.get_value("hu_sock_client_l1_source")
    https_client_post.post_param_value("hu", "self", "lidar_main", lidar_main)

def command_new_save():
    saving.determine_path()

def command_ssd_editing():
    param_co.state_co["path"]["file_name_add"] = dpg.get_value("ssd_path_add")
    param_co.path_ssd = dpg.get_value("ssd_path")
    saving.determine_path()

def command_combo_lidar():
    lidar_main = dpg.get_value("combo_lidar")
    param_co.lidar_main = lidar_main
    dpg.set_value("hu_sock_client_l1_source", lidar_main)
    command_lidar_source()

def command_comboip():
    hu_ip = wallet.get_ip_from_key(dpg.get_value("hu_wallet"))
    py_ip = wallet.get_ip_from_key(dpg.get_value("py_wallet"))
    ed_ip = wallet.get_ip_from_key(dpg.get_value("ed_wallet"))
    ve_ip = wallet.get_ip_from_key(dpg.get_value("ve_wallet"))
    ai_ip = wallet.get_ip_from_key(dpg.get_value("ai_wallet"))
    sncf_ip = wallet.get_ip_from_key(dpg.get_value("sncf_wallet"))
    l1_ip = wallet.get_ip_from_key(dpg.get_value("l1_wallet"))
    l2_ip = wallet.get_ip_from_key(dpg.get_value("l2_wallet"))

    if(hu_ip != None):
        param_co.state_co["hubium"]["ip"] = hu_ip
        dpg.set_value("hu_ip", hu_ip)
        https_client_con.test_hu_con()
        https_client_post.post_param_value("py", "hubium", "ip", hu_ip)
    if(py_ip != None):
        param_co.state_hu["pywardium"]["ip"] = py_ip
        dpg.set_value("py_ip", py_ip)
        https_client_post.post_param_value("hu", "pywardium", "ip", py_ip)
    if(ed_ip != None):
        param_co.state_hu["edge"]["ip"] = ed_ip
        dpg.set_value("ed_ip", ed_ip)
        https_client_post.post_param_value("hu", "edge", "ip", ed_ip)
    if(ve_ip != None):
        param_co.state_hu["velodium"]["ip"] = ve_ip
        dpg.set_value("ed_ip", ve_ip)
        https_client_post.post_param_value("hu", "velodium", "ip", ve_ip)
    if(ai_ip != None):
        param_co.state_hu["ai"]["ip"] = ai_ip
        dpg.set_value("ai_ip", ai_ip)
        https_client_post.post_param_value("hu", "ai", "ip", ai_ip)
    if(sncf_ip != None):
        param_co.state_hu["sncf"]["broker_ip"] = sncf_ip
        dpg.set_value("sncf_ip", sncf_ip)
        https_client_post.post_param_value("hu", "sncf", "broker_ip", sncf_ip)
    if(l1_ip != None):
        param_co.state_py["lidar_1"]["ip"] = l1_ip
        dpg.set_value("l1_ip", l1_ip)
        https_client_post.post_param_value("py", "lidar_1", "ip", l1_ip)
    if(l2_ip != None):
        param_co.state_py["lidar_2"]["ip"] = l2_ip
        dpg.set_value("l2_ip", l2_ip)
        https_client_post.post_param_value("py", "lidar_2", "ip", l2_ip)

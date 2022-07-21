#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_get
from HTTP import http_client_post
from src import saving
from src import parser_json
from src import wallet

import dearpygui.dearpygui as dpg


def callback_choice_port():
    http_client_post.post_param_py("controlium", "sock_server_port", dpg.get_value("co_sock_server_port"))
    http_client_post.post_param_py("pywardium", "http_server_port", dpg.get_value("py_http_server_port"))
    http_client_post.post_param_hu("self", "sock_server_port", dpg.get_value("hu_sock_server_port"))
    http_client_post.post_param_hu("sncf", "broker_port", dpg.get_value("sncf_broker_port"))

def callback_update_conf():
    pass

def callback_lidar():
    http_client_post.post_param_py("lidar_1", "activated", dpg.get_value("l1_activated"))
    http_client_post.post_param_py("lidar_1", "speed", dpg.get_value("l1_speed"))
    http_client_post.post_param_py("lidar_1", "ip", str(dpg.get_value("l1_ip")))
    http_client_post.post_param_py("lidar_2", "activated", dpg.get_value("l2_activated"))
    http_client_post.post_param_py("lidar_2", "speed", dpg.get_value("l2_speed"))
    http_client_post.post_param_py("lidar_2", "ip", str(dpg.get_value("l2_ip")))

def callback_l1_start():
    http_client_post.post_lidar_start("lidar_1")

def callback_l1_stopt():
    http_client_post.post_lidar_stop("lidar_1")

def callback_l2_start():
    http_client_post.post_lidar_start("lidar_2")

def callback_l2_stopt():
    http_client_post.post_lidar_stop("lidar_2")

def callback_false_alarm():
    http_client_get.get_falsealarm()

def callback_ssd():
    param_co.path_ssd = dpg.get_value("ssd_path")
    param_co.state_co["ssd"]["activated"] = dpg.get_value("ssd_active")
    param_co.state_co["path"]["file_name_add"] = dpg.get_value("ssd_path_add")
    saving.determine_path()

def callback_param_py():
    http_client_post.post_param_py("lidar_1", "device", str(dpg.get_value("py_l1_device")))
    http_client_post.post_param_py("lidar_2", "device", str(dpg.get_value("py_l2_device")))
    http_client_post.post_param_py("self", "http_server_port", dpg.get_value("py_http_server_port"))

def callback_comboip():
    hu_ip = wallet.get_ip_from_key(dpg.get_value("hu_wallet"))
    py_ip = wallet.get_ip_from_key(dpg.get_value("py_wallet"))
    ed_ip = wallet.get_ip_from_key(dpg.get_value("ed_wallet"))
    sncf_ip = wallet.get_ip_from_key(dpg.get_value("sncf_wallet"))

    if(hu_ip != None):
        param_co.state_co["hubium"]["ip"] = hu_ip
        dpg.set_value("hu_ip", hu_ip)
    if(py_ip != None):
        param_co.state_py["self"]["ip"] = py_ip
        dpg.set_value("py_ip", py_ip)
        http_client_post.post_param_hu("pywardium", "ip", py_ip)
    if(ed_ip != None):
        param_co.state_hu["edge"]["ip"] = ed_ip
        dpg.set_value("ed_ip", ed_ip)
        http_client_post.post_param_hu("edge", "ip", ed_ip)
    if(sncf_ip != None):
        param_co.state_hu["sncf"]["broker_ip"] = sncf_ip
        dpg.set_value("sncf_ip", sncf_ip)
        http_client_post.post_param_hu("sncf", "broker_ip", sncf_ip)

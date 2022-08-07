#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_get
from HTTP import http_client_post
from SOCK import sock_server
from src import saving
from src import parser_json
from src import wallet

import dearpygui.dearpygui as dpg


def callback_port_controlium():
    param_co.state_co["self"]["sock_server_l1_port"] = dpg.get_value("co_sock_server_l1_port")
    param_co.state_co["self"]["sock_server_l2_port"] = dpg.get_value("co_sock_server_l2_port")
    http_client_post.post_param_hu("controlium", "sock_server_l1_port", dpg.get_value("co_sock_server_l1_port"))
    http_client_post.post_param_hu("controlium", "sock_server_l2_port", dpg.get_value("co_sock_server_l2_port"))
    sock_server.restart_daemon()
def callback_port_hubium():
    http_client_post.post_param_hu("self", "sock_server_l1_port", dpg.get_value("hu_sock_server_l1_port"))
    http_client_post.post_param_hu("self", "sock_server_l2_port", dpg.get_value("hu_sock_server_l2_port"))
    http_client_post.post_param_hu("sncf", "broker_port", dpg.get_value("sncf_broker_port"))
    http_client_post.post_param_hu("sncf", "mqtt_topic", dpg.get_value("sncf_mqtt_topic"))
    http_client_post.post_param_py("hubium", "sock_server_l1_port", dpg.get_value("hu_sock_server_l1_port"))
    http_client_post.post_param_py("hubium", "sock_server_l2_port", dpg.get_value("hu_sock_server_l2_port"))
    http_client_get.get_restart_sock_server()
def callback_port_pywardium():
    http_client_post.post_param_py("pywardium", "http_server_port", dpg.get_value("py_http_server_port"))

def callback_lidar_active():
    http_client_post.post_param_py("lidar_1", "activated", dpg.get_value("l1_activated"))
    http_client_post.post_param_py("lidar_2", "activated", dpg.get_value("l2_activated"))
def callback_lidar_ip():
    http_client_post.post_param_py("lidar_1", "ip", str(dpg.get_value("l1_ip")))
    http_client_post.post_param_py("lidar_2", "ip", str(dpg.get_value("l2_ip")))
def callback_lidar_speed():
    http_client_post.post_param_py("lidar_1", "ip", str(dpg.get_value("l1_ip")))
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
    http_client_get.get_false_alarm()
def callback_new_save():
    saving.determine_path()
def callback_ssd():
    param_co.path_ssd = dpg.get_value("ssd_path")
    param_co.state_co["ssd"]["activated"] = dpg.get_value("ssd_active")
def callback_name_editing():
    dpg.set_value("ssd_active", False)
    param_co.state_co["ssd"]["activated"] = False
    param_co.state_co["path"]["file_name_add"] = dpg.get_value("ssd_path_add")
    param_co.path_ssd = dpg.get_value("ssd_path")
    saving.determine_path()
def callback_param_py():
    l1_dev = dpg.get_value("py_l1_device")
    l2_dev = dpg.get_value("py_l2_device")
    param_co.state_py["lidar_1"]["device"] = l1_dev
    param_co.state_py["lidar_2"]["device"] = l2_dev
    http_client_post.post_param_py("lidar_1", "device", str(l1_dev))
    http_client_post.post_param_py("lidar_2", "device", str(l2_dev))
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
        param_co.state_hu["pywardium"]["ip"] = py_ip
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

def callback_hubium_source():
    source_l1 = dpg.get_value("hu_sock_client_l1_source")
    if(source_l1 == "Lidar 1"):
        source_l2 = "Lidar 2"
    else:
        source_l2 = "Lidar 1"
    dpg.set_value("hu_sock_client_l2_source", source_l2)
    http_client_post.post_param_hu("self", "sock_server_l1_source", source_l1)
    http_client_post.post_param_hu("self", "sock_server_l2_source", source_l2)
def callback_velo_option():
    opt_slam = dpg.get_value("ve_opt_slam")
    http_client_post.post_param_ve("slam", opt_slam)

    opt_view = dpg.get_value("ve_opt_view")
    http_client_post.post_param_ve("view", opt_view)

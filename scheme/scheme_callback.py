#! /usr/bin/python
#---------------------------------------------

from param import param_co
from HTTP import http_client_get
from HTTP import http_client_post
from SOCK import sock_server

import dearpygui.dearpygui as dpg


def callback_hubium():
    param_co.state_hu["self"]["sock_server_l1_port"] = dpg.get_value("hu_sock_server_l1_port")
    param_co.state_hu["self"]["sock_server_l2_port"] = dpg.get_value("hu_sock_server_l2_port")
    param_co.state_hu["self"]["sock_server_l1_port"] = dpg.get_value("hu_sock_server_l1_port")
    param_co.state_hu["self"]["sock_server_l2_port"] = dpg.get_value("hu_sock_server_l2_port")
    param_co.state_hu["sncf"]["broker_port"] = dpg.get_value("sncf_broker_port")
    param_co.state_hu["sncf"]["mqtt_topic"] = dpg.get_value("sncf_mqtt_topic")
    param_co.state_hu["sncf"]["mqtt_client_name"] = dpg.get_value("hu_mqtt_client_name")
    http_client_post.send_hu_state()

def callback_controlium():
    param_co.state_co["self"]["sock_server_l1_port"] = dpg.get_value("co_sock_server_l1_port")
    param_co.state_co["self"]["sock_server_l2_port"] = dpg.get_value("co_sock_server_l2_port")
    sock_server.restart_daemon()

    param_co.state_hu["controlium"]["sock_server_l1_port"] = dpg.get_value("co_sock_server_l1_port")
    param_co.state_hu["controlium"]["sock_server_l2_port"] = dpg.get_value("co_sock_server_l2_port")
    http_client_post.send_hu_state()

def callback_pywardium():
    param_co.state_py["self"]["http_server_port"] = dpg.get_value("py_http_server_port")
    param_co.state_py["lidar_1"]["activated"] = dpg.get_value("l1_activated")
    param_co.state_py["lidar_1"]["ip"] = dpg.get_value("l1_ip")
    param_co.state_py["lidar_1"]["speed"] = dpg.get_value("l1_speed")
    param_co.state_py["lidar_1"]["device"] = dpg.get_value("py_l1_device")
    param_co.state_py["lidar_2"]["activated"] = dpg.get_value("l2_activated")
    param_co.state_py["lidar_2"]["ip"] = dpg.get_value("l2_ip")
    param_co.state_py["lidar_2"]["speed"] = dpg.get_value("l2_speed")
    param_co.state_py["lidar_2"]["device"] = dpg.get_value("py_l2_device")
    http_client_post.send_py_state()

def callback_velodium():
    http_client_post.post_param_ve("slam", dpg.get_value("ve_opt_slam"))
    http_client_post.post_param_ve("view", dpg.get_value("ve_opt_view"))

def callback_ai():
    http_client_post.post_param_ai("lidar_height", dpg.get_value("ai_lidar_height"))
    http_client_post.post_param_ai("threshold", dpg.get_value("ai_threshold"))

def callback_ssd():
    param_co.path_ssd = dpg.get_value("ssd_path")
    param_co.state_co["ssd"]["activated"] = dpg.get_value("ssd_active")

#! /usr/bin/python
#---------------------------------------------

from param import param_co
from scheme import scheme_link

import dearpygui.dearpygui as dpg


def update():
    scheme_link.update_link_color()
    update_ssd()
    update_train()
    update_controlium()
    update_hubium()
    update_pywardium()
    update_data()

def update_ssd():
    dpg.set_value("ssd_path", param_co.path_ssd)
    dpg.set_value("ssd_total", param_co.state_co["ssd"]["space_total"])
    dpg.set_value("ssd_used", param_co.state_co["ssd"]["space_used"])
    dpg.set_value("l1_file_path", param_co.state_py["lidar_1"]["dir"])
    dpg.set_value("l2_file_path", param_co.state_py["lidar_2"]["dir"])
    dpg.set_value("file_name", param_co.state_py["path"]["name"])

def update_train():
    dpg.set_value("l1_ip", param_co.state_py["lidar_1"]["ip"])
    dpg.set_value("l2_ip", param_co.state_py["lidar_1"]["ip"])
    dpg.set_value("geo_country", param_co.state_py["geolocalization"]["country"])

def update_controlium():
    dpg.set_value("co_status", param_co.state_co["self"]["status"])
    dpg.set_value("co_ip", param_co.state_co["self"]["ip"])
    dpg.set_value("co_sock_server_port", param_co.state_co["self"]["sock_server_port"])

def update_hubium():
    dpg.set_value("hu_status", param_co.state_hu["self"]["status"])
    dpg.set_value("hu_ip", param_co.state_co["self"]["ip"])
    dpg.set_value("ve_sock_server_port", param_co.state_hu["velodium"]["sock_server_port"])
    dpg.set_value("hu_sock_server_port", param_co.state_hu["self"]["sock_server_port"])
    dpg.set_value("hu_http_server_port", param_co.state_hu["self"]["http_server_port"])
    dpg.set_value("sncf_broker_port", param_co.state_hu["sncf"]["broker_port"])
    dpg.set_value("sncf_mqtt_topic", param_co.state_hu["sncf"]["mqtt_topic"])

def update_pywardium():
    dpg.set_value("py_status", param_co.state_py["self"]["status"])
    dpg.set_value("py_ip", param_co.state_co["self"]["ip"])
    dpg.set_value("py_l1_device", param_co.state_py["lidar_1"]["device"])
    dpg.set_value("py_l2_device", param_co.state_py["lidar_2"]["device"])

def update_data():
    dpg.set_value("nb_frame", param_co.state_hu["self"]["nb_frame"])
    dpg.set_value("nb_prediction", param_co.state_hu["self"]["nb_prediction"])

def update_image():
    width, height, channels, data = dpg.load_image(param_co.path_image)
    dpg.set_value("image_in", data)

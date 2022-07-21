#! /usr/bin/python
#---------------------------------------------

from param import param_co
from src import io
from scheme import scheme_link
from scheme import scheme_plot

import dearpygui.dearpygui as dpg


def update():
    scheme_link.update_link_color()
    update_ssd()
    update_train()
    update_controlium()
    update_hubium()
    update_edge()
    update_pywardium()
    update_data()

def update_ssd():
    dpg.set_value("ssd_path", param_co.path_ssd)
    dpg.set_value("ssd_total", param_co.state_co["ssd"]["space_total"])
    dpg.set_value("ssd_used", param_co.state_co["ssd"]["space_used"])
    dpg.set_value("l1_file_path", param_co.state_co["path"]["dir_l1"])
    dpg.set_value("l2_file_path", param_co.state_co["path"]["dir_l2"])
    dpg.set_value("file_name", param_co.state_co["path"]["file_name"])

def update_train():
    dpg.set_value("l1_ip", param_co.state_py["lidar_1"]["ip"])
    dpg.set_value("l2_ip", param_co.state_py["lidar_2"]["ip"])
    dpg.set_value("l1_bandwidth", param_co.state_py["lidar_1"]["bandwidth"])
    dpg.set_value("l2_bandwidth", param_co.state_py["lidar_2"]["bandwidth"])
    dpg.set_value("geo_country", param_co.state_py["geolocalization"]["country"])

def update_controlium():
    dpg.set_value("co_status", param_co.state_co["self"]["status"])
    dpg.set_value("co_ip", param_co.state_co["self"]["ip"])
    dpg.set_value("co_thread", param_co.state_co["self"]["nb_thread"])
    dpg.set_value("co_sock_server_l1_port", param_co.state_co["self"]["sock_server_l1_port"])
    dpg.set_value("co_sock_server_l2_port", param_co.state_co["self"]["sock_server_l2_port"])

def update_hubium():
    dpg.set_value("hu_status", param_co.state_hu["self"]["status"])
    dpg.set_value("hu_ip", param_co.state_co["hubium"]["ip"])
    dpg.set_value("hu_thread", param_co.state_hu["self"]["nb_thread"])

    dpg.set_value("hu_country", param_co.state_hu["self"]["country"])
    dpg.set_value("hu_edge_id", param_co.state_hu["self"]["edge_id"])
    dpg.set_value("ve_sock_server_port", param_co.state_hu["velodium"]["sock_server_port"])
    dpg.set_value("ai_http_server_port", param_co.state_hu["ai"]["http_server_port"])
    dpg.set_value("hu_sock_server_l1_port", param_co.state_hu["self"]["sock_server_l1_port"])
    dpg.set_value("hu_sock_server_l2_port", param_co.state_hu["self"]["sock_server_l2_port"])
    dpg.set_value("hu_http_server_port", param_co.state_hu["self"]["http_server_port"])
    dpg.set_value("sncf_broker_port", param_co.state_hu["sncf"]["broker_port"])
    dpg.set_value("sncf_mqtt_topic", param_co.state_hu["sncf"]["mqtt_topic"])

def update_edge():
    dpg.set_value("ed_country", param_co.state_hu["edge"]["country"])
    dpg.set_value("ed_edge_id", param_co.state_hu["edge"]["edge_id"])
    dpg.set_value("ed_sock_server_port", param_co.state_hu["self"]["sock_server_l1_port"])
    dpg.set_value("ed_http_server_port", param_co.state_hu["self"]["http_server_port"])

def update_pywardium():
    dpg.set_value("py_status", param_co.state_py["self"]["status"])
    dpg.set_value("py_ip", param_co.state_py["self"]["ip"])
    dpg.set_value("py_thread", param_co.state_py["self"]["nb_thread"])
    dpg.set_value("py_http_server_port", int(param_co.state_py["self"]["http_server_port"]))

    devices = io.get_list_device_from_state()
    dpg.configure_item("py_l1_device",items=devices, num_items=len(devices))
    dpg.configure_item("py_l2_device",items=devices, num_items=len(devices))

def update_data():
    dpg.set_value("nb_frame", param_co.state_hu["self"]["nb_frame"])
    dpg.set_value("nb_prediction", param_co.state_hu["self"]["nb_prediction"])
    #scheme_plot.update_plot_random()

def update_image():
    width, height, channels, data = dpg.load_image(param_co.path_image)
    dpg.set_value("image_in", data)

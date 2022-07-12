#! /usr/bin/python
#---------------------------------------------

from param import cla
from scheme import scheme_link

import dearpygui.dearpygui as dpg


def update():
    scheme_link.update_link_color()
    update_ssd_info()
    update_status()
    update_port()
    update_train()
    update_data()

def update_ssd_info():
    dpg.set_value("ssd_path", cla.contro.ssd_path)
    dpg.set_value("ssd_total", cla.contro.ssd_space_total)
    dpg.set_value("ssd_used", cla.contro.ssd_space_used)
    dpg.set_value("l1_file_path", cla.lidars.path_dir_l1)
    dpg.set_value("l2_file_path", cla.lidars.path_dir_l2)
    dpg.set_value("file_name", cla.lidars.file_name)

def update_train():
    dpg.set_value("l1_ip", cla.lidars.l1_ip)
    dpg.set_value("l2_ip", cla.lidars.l2_ip)
    dpg.set_value("geo_country", cla.pyward.geo_country)

def update_port():
    # Controlium
    dpg.set_value("co_sock_server_port", cla.contro.port_sock_server)

    # Hubium
    dpg.set_value("ve_sock_server_port", cla.hubium.velo_sock_server_port)
    dpg.set_value("hu_sock_server_port", cla.hubium.sock_server_port)
    dpg.set_value("hu_http_server_port", cla.hubium.http_server_port)
    dpg.set_value("ed_sock_client_port", cla.hubium.edge_port)

    # SNCF
    dpg.set_value("sncf_broker_port", cla.hubium.sncf_broker_port)
    dpg.set_value("sncf_broker_port", cla.hubium.sncf_broker_port)
    dpg.set_value("sncf_mqtt_topic", cla.hubium.sncf_mqtt_topic)

    # Pywardium
    #dpg.set_value("py_sock_client_port", cla.pyward.sock_server_port)

    # Lidar
    #dpg.set_value("py_device_l1_port", cla.lidars.l1_device)
    #dpg.set_value("py_device_l2_port", cla.lidars.l2_device)

def update_status():
    dpg.set_value("co_status", cla.contro.status)
    dpg.set_value("py_status", cla.pyward.status)
    dpg.set_value("hu_status", cla.hubium.status)
    dpg.set_value("co_ip", cla.contro.ip)
    dpg.set_value("py_ip", cla.pyward.ip)
    dpg.set_value("hu_ip", cla.hubium.ip)

def update_data():
    dpg.set_value("nb_frame", cla.hubium.nb_frame)
    dpg.set_value("nb_prediction", cla.hubium.nb_prediction)

def update_image():
    width, height, channels, data = dpg.load_image(cla.contro.path_image)
    dpg.set_value("image_in", data)

#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import classes
from scheme import scheme_link

import dearpygui.dearpygui as dpg


def update():
    scheme_link.update_link_color()
    update_ssd_info()
    update_status()
    update_port()
    update_train()

def update_ssd_info():
    dpg.set_value("ssd_path", param_co.ssd_path)
    dpg.set_value("ssd_total", param_co.ssd_space_total)
    dpg.set_value("ssd_used", param_co.ssd_space_used)
    dpg.set_value("l1_file_path", classes.lidars.path_dir_l1)
    dpg.set_value("l2_file_path", classes.lidars.path_dir_l2)
    dpg.set_value("file_name", classes.lidars.file_name)

def update_train():
    dpg.set_value("l1_ip", classes.lidars.l1_ip)
    dpg.set_value("l2_ip", classes.lidars.l2_ip)
    dpg.set_value("geo_country", classes.pyward.geo_country)

def update_port():
    # Controlium
    dpg.set_value("co_sock_server_port", param_co.port_sock_server)

    # Hubium
    dpg.set_value("va_http_client_port", classes.hubium.valeo_port)
    dpg.set_value("ve_sock_server_port", classes.hubium.velo_port)
    dpg.set_value("hu_sock_server_port", classes.hubium.sock_server_port)
    dpg.set_value("hu_sock_client_port", classes.hubium.sock_client_port)
    dpg.set_value("hu_http_server_port", classes.hubium.http_server_port)
    dpg.set_value("ed_sock_client_port", classes.hubium.edge_port)
    dpg.set_value("sncf_mqtt_port", classes.hubium.mqtt_port)

    # Pywardium
    dpg.set_value("py_sock_client_port", classes.pyward.sock_server_port)

    # Lidar
    #dpg.set_value("py_device_l1_port", classes.lidars.l1_device)
    #dpg.set_value("py_device_l2_port", classes.lidars.l2_device)

def update_status():
    dpg.set_value("co_status", param_co.status)
    dpg.set_value("py_status", classes.pyward.status)
    dpg.set_value("hu_status", classes.hubium.status)
    dpg.set_value("co_ip", param_co.ip)
    dpg.set_value("py_ip", classes.pyward.ip)
    dpg.set_value("hu_ip", classes.hubium.ip)

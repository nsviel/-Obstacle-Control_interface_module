#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import param_py
from param import param_hu
from param import param_li

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
    dpg.set_value("l1_file_path", param_li.path_dir_l1)
    dpg.set_value("l2_file_path", param_li.path_dir_l2)
    dpg.set_value("file_name", param_li.file_name)

def update_train():
    dpg.set_value("l1_ip", param_li.l1_ip)
    dpg.set_value("l2_ip", param_li.l2_ip)

def update_port():
    # Controlium
    dpg.set_value("co_sock_server_port", param_co.port_sock_server)

    # Hubium
    dpg.set_value("va_http_client_port", param_hu.valeo_port)
    dpg.set_value("ve_sock_server_port", param_hu.velo_port)
    dpg.set_value("hu_sock_server_port", param_hu.sock_server_port)
    dpg.set_value("hu_sock_client_port", param_hu.sock_client_port)
    dpg.set_value("hu_http_server_port", param_hu.http_server_port)
    dpg.set_value("ed_sock_client_port", param_hu.edge_port)
    dpg.set_value("sncf_mqtt_port", param_hu.mqtt_port)

    # Pywardium
    dpg.set_value("py_sock_client_port", param_py.sock_server_port)

    # Lidar
    #dpg.set_value("py_device_l1_port", param_li.l1_device)
    #dpg.set_value("py_device_l2_port", param_li.l2_device)

def update_status():
    dpg.set_value("co_status", param_co.status)
    dpg.set_value("py_status", param_py.status)
    dpg.set_value("hu_status", param_hu.status)
    dpg.set_value("co_ip", param_co.ip)
    dpg.set_value("py_ip", param_py.ip)
    dpg.set_value("hu_ip", param_hu.ip)

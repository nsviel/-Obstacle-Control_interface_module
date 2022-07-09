#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import param_py
from param import param_hu
from param import param_li

from scheme import scheme_link

import dearpygui.dearpygui as dpg


def update_gui():
    scheme_link.update_link_color()
    update_ssd_info()
    update_status()
    update_port()
    update_ip()

def update_ssd_info():
    dpg.set_value("ssd_total", param_co.ssd_space_total)
    dpg.set_value("ssd_used", param_co.ssd_space_used)

def update_status():
    dpg.set_value("co_status", param_co.status)
    dpg.set_value("py_status", param_py.status)
    dpg.set_value("hu_status", param_hu.status)

def update_port():
    # Controlium
    dpg.set_value("co_sock_server_val", param_co.port_sock_server)

    # Hubium
    dpg.set_value("va_port", param_hu.valeo_port)
    dpg.set_value("ve_port", param_hu.velo_port)
    dpg.set_value("hu_sock_server_val", param_hu.sock_server_port)
    dpg.set_value("hu_sock_client_val", param_hu.sock_client_port)
    dpg.set_value("hu_http_server_val", param_hu.http_server_port)
    dpg.set_value("ed_port", param_hu.edge_port)
    dpg.set_value("sncf_port", param_hu.mqtt_port)

    # Pywardium
    dpg.set_value("py_port_sock_val", param_py.sock_server_port)

    # Lidar
    dpg.set_value("py_device_l1_val", param_li.device_l1)
    dpg.set_value("py_device_l2_val", param_li.device_l2)

def update_ip():
    dpg.set_value("co_ip", param_co.ip)
    dpg.set_value("py_status", param_py.ip)
    dpg.set_value("hu_status", param_hu.ip)

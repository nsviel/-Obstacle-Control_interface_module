#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import param_py
from param import param_hu
from param import param_li

from gui import scheme_color

import dearpygui.dearpygui as dpg


def create_link():
    dpg.add_node_link("co_http_client", "hu_http_server", tag="link_co_hu")
    dpg.add_node_link("co_http_client", "ed_http_server", tag="link_co_ed")

    dpg.add_node_link("py_sock_client", "hu_sock_server_in", tag="link_py_hu_sock")
    dpg.add_node_link("py_http_server", "hu_http_client", tag="link_py_hu_http")
    dpg.add_node_link("py_server", "ssd_input", tag="link_py_ssd")
    dpg.add_node_link("py_device_l1", "l1_input", tag="link_py_l1")
    dpg.add_node_link("py_device_l2", "l2_input", tag="link_py_l2")
    dpg.add_node_link("py_server", "geo_input", tag="link_py_geo")

    dpg.add_node_link("hu_mqtt", "sncf_mqtt_port", tag="link_hu_sncf")
    dpg.add_node_link("hu_sock_client", "ed_server", tag="link_hu_ed")
    dpg.add_node_link("hu_sock_server_out", "ed_client", tag="link_ed_hu")
    dpg.add_node_link("hu_sock_client", "ve_input", tag="link_hu_ve")
    dpg.add_node_link("hu_stockage", "ai_input", tag="link_hu_ai")

    dpg.add_node_link("va_httpd_port", "hu_http_server", tag="link_va_hu")

def update_link_color():
    # Controlium connections
    update_link(param_co.http_connected, "link_co_hu")

    # Pywardium connections
    update_link(param_py.http_connected, "link_py_hu_http")
    update_link(param_py.socket_connected, "link_py_hu_sock")
    update_link(param_py.ssd_connected, "link_py_ssd")
    update_link(param_li.l1_connected, "link_py_l1")
    update_link(param_li.l2_connected, "link_py_l2")

    # Hubium connections
    update_link(param_hu.mqtt_connected, "link_hu_sncf")
    update_link(param_hu.velo_connected, "link_hu_ve")


    #update_link(param_hu.hubium_json['velo_connected'], "link_hu_ve")
    #update_link(param_hu.hubium_json['vale_connected'], "link_va_hu")
    #update_link(param_hu.hubium_json['ia_connectes'], "link_hu_ai")
    #update_link(param_hu.hubium_json['edge_conncted'], "link_hu_ed")

def update_link(state, tag):
    if(state):
        green = scheme_color.color_green()
        dpg.bind_item_theme(tag, green)
    else:
        red = scheme_color.color_red()
        dpg.bind_item_theme(tag, red)

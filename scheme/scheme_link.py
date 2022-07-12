#! /usr/bin/python
#---------------------------------------------

from param import param_co
from scheme import scheme_color

import dearpygui.dearpygui as dpg


def create_link():
    dpg.add_node_link("co_http_client", "hu_http_server_i", tag="link_co_hu_http")
    dpg.add_node_link("co_http_client", "ed_http_server", tag="link_co_ed_http")
    dpg.add_node_link("co_sock_server", "ed_sock_client", tag="link_co_ed_sock")
    dpg.add_node_link("co_sock_server", "hu_sock_client_i", tag="link_co_hu_sock")
    dpg.add_node_link("co_self", "ssd_input", tag="link_co_ssd")

    dpg.add_node_link("py_sock_client", "hu_sock_server_i", tag="link_py_hu_sock")
    dpg.add_node_link("py_http_server", "hu_http_client_i", tag="link_py_hu_http")
    dpg.add_node_link("py_l1_device", "l1_input", tag="link_py_l1")
    dpg.add_node_link("py_l2_device", "l2_input", tag="link_py_l2")
    dpg.add_node_link("py_self", "geo_input", tag="link_py_geo")

    dpg.add_node_link("hu_mqtt", "sncf_mqtt_broker", tag="link_hu_sncf_mqtt")
    dpg.add_node_link("hu_sock_client_o", "ed_sock_server", tag="link_hu_ed_sock")
    dpg.add_node_link("hu_sock_client_o", "ve_sock_server", tag="link_hu_ve_sock")
    dpg.add_node_link("hu_sock_server_o", "ed_sock_client", tag="link_ed_hu_sock")
    dpg.add_node_link("hu_stockage", "ai_input", tag="link_hu_ai")

    dpg.add_node_link("va_http_client", "hu_http_server_o", tag="link_va_hu")

def update_link_color():
    pass
    # Controlium
    update_link(param_co.state_co["hubium"]["connected"], "link_co_hu_http")
    update_link(param_co.state_co["ssd"]["connected"], "link_co_ssd")

    # Pywardium
    #update_link(cla.pyward.http_connected, "link_py_hu_http")
    #update_link(cla.pyward.socket_connected, "link_py_hu_sock")

    #update_link(cla.lidars.l1_connected, "link_py_l1")
    #update_link(cla.lidars.l2_connected, "link_py_l2")

    # Hubium
    update_link(param_co.state_hu["sncf"]["connected"], "link_hu_sncf_mqtt")
    update_link(param_co.state_hu["velodium"]["connected"], "link_hu_ve_sock")


def update_link(state, tag):
    if(state):
        green = scheme_color.color_green()
        dpg.bind_item_theme(tag, green)
    else:
        red = scheme_color.color_red()
        dpg.bind_item_theme(tag, red)

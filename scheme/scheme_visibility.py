#---------------------------------------------
from param import param_co
from HTTPS import https_client_get
from HTTPS import https_client_post
from SOCK import sock_server

import dearpygui.dearpygui as dpg


def set_mode():
    if(param_co.status_ui == "Development"):
        set_mode_dev()
    elif(param_co.status_ui == "Demo"):
        set_mode_demo()

def set_mode_dev():
    dpg.show_item("co_temp_visibile")
    dpg.show_item("ai_sncf_port_visible")
    dpg.show_item("hu_mqtt_visible")
    dpg.show_item("sncf_mqtt_topic_visible")

    dpg.show_item("co_thread_visible")
    dpg.show_item("hu_thread_visible")
    dpg.show_item("py_thread_visible")

    dpg.show_item("py_http_port_visible")
    dpg.show_item("hu_http_port_visible")
    dpg.show_item("ed_http_port_visible")
    dpg.show_item("ve_http_port_visible")
    dpg.show_item("ai_http_port_visible")

    dpg.show_item("l1_visible")
    dpg.show_item("l2_visible")
    dpg.show_item("co_port_l1_visible")
    dpg.show_item("co_port_l2_visible")
    dpg.show_item("hu_port_l1_visible")
    dpg.show_item("hu_port_l2_visible")
    dpg.show_item("py_l1_port_visible")
    dpg.show_item("py_l2_port_visible")

    dpg.show_item("ed_sock_port_visible")
    dpg.show_item("ve_sock_port_visible")

def set_mode_demo():
    dpg.hide_item("co_temp_visibile")
    dpg.hide_item("ai_sncf_port_visible")
    dpg.hide_item("hu_mqtt_visible")
    dpg.hide_item("sncf_mqtt_topic_visible")

    dpg.hide_item("co_thread_visible")
    dpg.hide_item("hu_thread_visible")
    dpg.hide_item("py_thread_visible")

    dpg.hide_item("py_http_port_visible")
    dpg.hide_item("hu_http_port_visible")
    dpg.hide_item("ed_http_port_visible")
    dpg.hide_item("ve_http_port_visible")
    dpg.hide_item("ai_http_port_visible")

    dpg.hide_item("l1_visible")
    dpg.hide_item("l2_visible")
    dpg.hide_item("co_port_l1_visible")
    dpg.hide_item("co_port_l2_visible")
    dpg.hide_item("hu_port_l1_visible")
    dpg.hide_item("hu_port_l2_visible")
    dpg.hide_item("py_l1_port_visible")
    dpg.hide_item("py_l2_port_visible")

    dpg.hide_item("ed_sock_port_visible")
    dpg.hide_item("ve_sock_port_visible")

#---------------------------------------------
from param import param_co
from scheme import scheme_color

import dearpygui.dearpygui as dpg


def create_link():
    dpg.add_node_link("co_http_client", "hu_http_server_i", tag="link_co_hu_http")
    dpg.add_node_link("co_sock_server_l1", "hu_sock_client_l1_i", tag="link_hu_co_l1_sock")
    dpg.add_node_link("co_sock_server_l2", "hu_sock_client_l2_i", tag="link_hu_co_l2_sock")
    dpg.add_node_link("co_self", "ssd_input", tag="link_co_ssd")

    dpg.add_node_link("hu_mqtt_client", "sncf_mqtt_broker", tag="link_hu_sncf_mqtt")
    dpg.add_node_link("hu_http_client_o", "ai_http_server", tag="link_ai_hu_http")
    dpg.add_node_link("hu_http_client_o", "ve_http_server", tag="link_hu_ve_http")
    dpg.add_node_link("hu_http_client_o", "ed_http_server", tag="link_hu_ed_http")
    dpg.add_node_link("hu_http_server_o", "ed_http_client", tag="link_ed_hu_http")

    dpg.add_node_link("hu_sock_client_l1_o", "ve_sock_server", tag="link_hu_ve_sock")
    dpg.add_node_link("hu_sock_client_l1_o", "ed_sock_server", tag="link_hu_ed_sock")
    dpg.add_node_link("hu_sock_server_l1_o", "ed_sock_client", tag="link_ed_hu_sock")

    dpg.add_node_link("va_http_client", "hu_http_server_o", tag="link_va_hu")

    dpg.add_node_link("py_l1_out", "hu_sock_server_l1_i", tag="link_py_hu_l1_sock")
    dpg.add_node_link("py_l2_out", "hu_sock_server_l2_i", tag="link_py_hu_l2_sock")
    dpg.add_node_link("py_http_server", "hu_http_client_i", tag="link_hu_py_http")
    dpg.add_node_link("py_l1_in", "l1_input", tag="link_l1_py")
    dpg.add_node_link("py_l2_in", "l2_input", tag="link_l2_py")
    dpg.add_node_link("py_self", "geo_input", tag="link_py_geo")

def update_link_color():
    # Controlium
    update_link_con(param_co.state_co["hubium"]["http_connected"], "link_co_hu_http")
    update_link_con(param_co.state_co["ssd"]["connected"], "link_co_ssd")
    update_link_sock(param_co.state_co["hubium"]["sock_l1_connected"], "link_hu_co_l1_sock")
    update_link_sock(param_co.state_co["hubium"]["sock_l2_connected"], "link_hu_co_l2_sock")

    # Lidars
    update_link_sock(param_co.state_hu["pywardium"]["sock_l1_connected"], "link_py_hu_l1_sock")
    update_link_sock(param_co.state_hu["pywardium"]["sock_l2_connected"], "link_py_hu_l2_sock")

    # Pywardium
    update_link_sock(param_co.state_py["lidar_1"]["connected"] and param_co.state_py["lidar_1"]["activated"], "link_l1_py")
    update_link_sock(param_co.state_py["lidar_2"]["connected"] and param_co.state_py["lidar_2"]["activated"], "link_l2_py")

    # Hubium
    update_link_con(param_co.state_hu["sncf"]["broker_connected"], "link_hu_sncf_mqtt")
    update_link_con(param_co.state_hu["pywardium"]["http_connected"], "link_hu_py_http")
    update_link_con(param_co.state_hu["edge"]["http_connected"], "link_hu_ed_http")
    update_link_sock(param_co.state_hu["edge"]["sock_connected"], "link_hu_ed_sock")
    update_link_sock(param_co.state_hu["velodium"]["sock_connected"], "link_hu_ve_sock")
    update_link_con(param_co.state_hu["velodium"]["http_connected"], "link_hu_ve_http")

    # Edge
    update_link_con(param_co.state_hu["edge"]["http_connected"], "link_ed_hu_http")
    update_link_sock(param_co.state_hu["edge"]["sock_connected"], "link_ed_hu_sock")

    # Valeo
    update_link_con(param_co.state_hu["valeo"]["http_connected"], "link_va_hu")

    # AI
    update_link_con(param_co.state_hu["ai"]["http_connected"], "link_ai_hu_http")

def update_link_con(state, tag):
    if(state):
        conn = scheme_color.color_link_green()
        dpg.bind_item_theme(tag, conn)
    else:
        disconn = scheme_color.color_link_red()
        dpg.bind_item_theme(tag, disconn)

def update_link_sock(state, tag):
    if(state):
        conn = scheme_color.color_link_blue()
        dpg.bind_item_theme(tag, conn)
    else:
        disconn = scheme_color.color_link_whiteblue()
        dpg.bind_item_theme(tag, disconn)

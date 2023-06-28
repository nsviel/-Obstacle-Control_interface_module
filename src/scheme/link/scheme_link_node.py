#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_color

import dearpygui.dearpygui as dpg


def create_link_train():
    dpg.add_node_link("capture_l1_in", "l1_status", tag="link_l1_py")
    dpg.add_node_link("capture_l2_in", "l2_status", tag="link_l2_py")
    dpg.add_node_link("capture_input", "geo_status", tag="link_capture_geo")

def create_link_edge_1():
    # Inter Edge
    dpg.add_node_link("edge_1_mqtt_client", "trainope_mqtt_broker", tag="link_edge_trainope_mqtt")
    dpg.add_node_link("edge_1_http_client_i", "ai_http_server", tag="link_ai_edge_1_http")
    dpg.add_node_link("edge_1_http_client_i", "processing_http_server", tag="link_edge_processing_http")
    dpg.add_node_link("processing_sock_server", "edge_1_sock_client_l1_i", tag="link_edge_processing_sock")

    # Edge <-> Interface
    dpg.add_node_link("interface_http_client", "edge_1_http_server_o", tag="link_interface_edge_1_http")
    dpg.add_node_link("interface_sock_server_l1", "edge_1_sock_client_l1_o", tag="link_edge_interface_l1_sock")
    dpg.add_node_link("interface_sock_server_l2", "edge_1_sock_client_l2_o", tag="link_edge_interface_l2_sock")
    dpg.add_node_link("interface_input", "ssd_input", tag="link_interface_ssd")

    # Edge <-> cloud
    dpg.add_node_link("va_http_client", "edge_1_http_server_o", tag="link_va_hu")

    # Edge <-> train
    dpg.add_node_link("capture_l1_out", "edge_1_sock_server_l1_i", tag="link_capture_edge_l1_sock")
    dpg.add_node_link("capture_l2_out", "edge_1_sock_server_l2_i", tag="link_capture_edge_l2_sock")
    dpg.add_node_link("capture_http_server", "edge_1_http_client_i", tag="link_edge_capture_http")

def create_link_edge_2():
    pass
    # Interface <-> Edge 2
    #dpg.add_node_link("edge_1_http_client_o", "edge_2_http_server", tag="link_edge_edge_2_http")
    #dpg.add_node_link("edge_1_http_server_o", "edge_2_http_client", tag="link_edge_2_edge_1_http")
    #dpg.add_node_link("edge_2_sock_server_l1_i", "edge_1_sock_client_l1_o", tag="link_edge_edge_2_sock")
    #dpg.add_node_link("edge_2_sock_client_l1_i", "edge_1_sock_server_l1_o", tag="link_edge_2_edge_sock")

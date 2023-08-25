#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_color
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def create_link_train():
    dpg.add_node_link(object.object.capture.ID_sock_server_l1, object.object.train.ID_l1_status, tag="link_l1_py")
    dpg.add_node_link(object.object.capture.ID_sock_server_l2, object.object.train.ID_l2_status, tag="link_l2_py")
    dpg.add_node_link("interface_input", "ssd_input", tag="link_control_ssd_usb")

def create_link_edge_1():
    # Inter Edge
    dpg.add_node_link(object.object.edge_1.ID_http_client_i, object.object.edge_1.ai.ID_http_server, tag="link_edge_1_ai_http")
    dpg.add_node_link(object.object.edge_1.ID_http_client_i, object.object.edge_1.slam.ID_http_server, tag="link_edge_1_processing_http")
    dpg.add_node_link(object.object.edge_1.ID_sock_client_l1_i, object.object.edge_1.slam.ID_sock_server, tag="link_edge_1_processing_sock")

    # Edge <-> Control
    dpg.add_node_link(object.object.edge_1.ID_http_server_o, object.object.control.ID_http_client, tag="link_edge_1_control_http")
    dpg.add_node_link(object.object.edge_1.ID_sock_client_l1_o, object.object.control.ID_sock_server_l1, tag="link_edge_1_interface_l1_sock")
    dpg.add_node_link(object.object.edge_1.ID_sock_client_l2_o, object.object.control.ID_sock_server_l2, tag="link_edge_1_interface_l2_sock")

    # Edge <-> cloud
    dpg.add_node_link(object.object.edge_1.ID_http_server_o, "va_http_client", tag="link_edge_1_car_http")
    dpg.add_node_link(object.object.edge_1.ID_mqtt_client, object.object.operator.ID_mqtt_broker, tag="link_edge_1_trainope_mqtt")

    # Edge <-> capture
    dpg.add_node_link(object.object.edge_1.ID_sock_server_l1_i, object.object.capture.ID_sock_client_l1, tag="link_capture_edge_1_l1_sock")
    dpg.add_node_link(object.object.edge_1.ID_sock_server_l2_i, object.object.capture.ID_sock_client_l2, tag="link_capture_edge_1_l2_sock")
    dpg.add_node_link(object.object.edge_1.ID_http_client_i, object.object.capture.ID_http_server, tag="link_edge_1_capture_http")

def create_link_edge_2():
    # Inter Edge
    dpg.add_node_link(object.object.edge_2.ID_http_client_i, object.object.edge_1.ai.ID_http_server, tag="link_edge_2_ai_http")
    dpg.add_node_link(object.object.edge_2.ID_http_client_i, object.object.edge_1.slam.ID_http_server, tag="link_edge_2_processing_http")
    dpg.add_node_link(object.object.edge_2.ID_sock_client_l1_i, object.object.edge_1.slam.ID_sock_server, tag="link_edge_2_processing_sock")

    # Edge <-> Control
    dpg.add_node_link(object.object.edge_2.ID_http_server_o, object.object.control.ID_http_client, tag="link_edge_2_control_http")
    dpg.add_node_link(object.object.edge_2.ID_sock_client_l1_o, object.object.control.ID_sock_server_l1, tag="link_edge_2_interface_l1_sock")
    dpg.add_node_link(object.object.edge_2.ID_sock_client_l2_o, object.object.control.ID_sock_server_l2, tag="link_edge_2_interface_l2_sock")

    # Edge <-> cloud
    dpg.add_node_link(object.object.edge_2.ID_http_server_o, "va_http_client", tag="link_edge_2_car_http")
    dpg.add_node_link(object.object.edge_2.ID_mqtt_client, object.object.operator.ID_mqtt_broker, tag="link_edge_2_trainope_mqtt")

    # Edge <-> capture
    dpg.add_node_link(object.object.edge_2.ID_sock_server_l1_i, object.object.capture.ID_sock_client_l1, tag="link_capture_edge_2_l1_sock")
    dpg.add_node_link(object.object.edge_2.ID_sock_server_l2_i, object.object.capture.ID_sock_client_l2, tag="link_capture_edge_2_l2_sock")
    dpg.add_node_link(object.object.edge_2.ID_http_client_i, object.object.capture.ID_http_server, tag="link_edge_2_capture_http")

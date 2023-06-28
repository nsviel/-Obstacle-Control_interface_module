#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_color

import dearpygui.dearpygui as dpg


def create_link():
    # module_interface
    dpg.add_node_link("interface_http_client", "edge_http_server_o", tag="link_interface_edge_http")
    dpg.add_node_link("interface_sock_server_l1", "edge_sock_client_l1_o", tag="link_edge_interface_l1_sock")
    dpg.add_node_link("interface_sock_server_l2", "edge_sock_client_l2_o", tag="link_edge_interface_l2_sock")
    dpg.add_node_link("interface_input", "ssd_input", tag="link_interface_ssd")

    dpg.add_node_link("edge_mqtt_client", "trainope_mqtt_broker", tag="link_edge_trainope_mqtt")
    dpg.add_node_link("edge_http_client_i", "ai_http_server", tag="link_ai_edge_http")
    dpg.add_node_link("edge_http_client_i", "processing_http_server", tag="link_edge_processing_http")
    dpg.add_node_link("edge_http_client_o", "edgenext_http_server", tag="link_edge_edgenext_http")
    dpg.add_node_link("edge_http_server_o", "edgenext_http_client", tag="link_edgenext_edge_http")

    dpg.add_node_link("processing_sock_server", "edge_sock_client_l1_i", tag="link_edge_processing_sock")
    dpg.add_node_link("edgenext_sock_server", "edge_sock_client_l1_o", tag="link_edge_edgenext_sock")
    dpg.add_node_link("edgenext_sock_client", "edge_sock_server_l1_o", tag="link_edgenext_edge_sock")

    dpg.add_node_link("va_http_client", "edge_http_server_o", tag="link_va_hu")

    dpg.add_node_link("capture_l1_out", "edge_sock_server_l1_i", tag="link_capture_edge_l1_sock")
    dpg.add_node_link("capture_l2_out", "edge_sock_server_l2_i", tag="link_capture_edge_l2_sock")
    dpg.add_node_link("capture_http_server", "edge_http_client_i", tag="link_edge_capture_http")
    dpg.add_node_link("capture_l1_in", "l1_status", tag="link_l1_py")
    dpg.add_node_link("capture_l2_in", "l2_status", tag="link_l2_py")
    dpg.add_node_link("capture_input", "geo_status", tag="link_capture_geo")

def update_link_color():
    # module_interface
    update_link_con(param_interface.state_interface["edge"]["http_connected"], "link_interface_edge_http")
    update_link_con(param_interface.state_interface["ssd"]["connected"], "link_interface_ssd")
    update_link_sock(param_interface.state_interface["edge"]["sock_l1_connected"], "link_edge_interface_l1_sock")
    update_link_sock(param_interface.state_interface["edge"]["sock_l2_connected"], "link_edge_interface_l2_sock")

    # Lidars
    update_link_sock(param_interface.state_edge["module_capture"]["sock_l1_connected"], "link_capture_edge_l1_sock")
    update_link_sock(param_interface.state_edge["module_capture"]["sock_l2_connected"], "link_capture_edge_l2_sock")

    # module_capture
    update_link_sock(param_interface.state_capture["lidar_1"]["connected"] and param_interface.state_capture["lidar_1"]["activated"], "link_l1_py")
    update_link_sock(param_interface.state_capture["lidar_2"]["connected"] and param_interface.state_capture["lidar_2"]["activated"], "link_l2_py")

    # module_edge
    update_link_con(param_interface.state_edge["train_operator"]["broker_connected"], "link_edge_trainope_mqtt")
    update_link_con(param_interface.state_edge["module_capture"]["http_connected"], "link_edge_capture_http")
    update_link_con(param_interface.state_edge["edge_next"]["http_connected"], "link_edge_edgenext_http")
    update_link_sock(param_interface.state_edge["edge_next"]["sock_connected"], "link_edge_edgenext_sock")
    update_link_sock(param_interface.state_edge["component_process"]["sock_connected"], "link_edge_processing_sock")
    update_link_con(param_interface.state_edge["component_process"]["http_connected"], "link_edge_processing_http")

    # Edge
    update_link_con(param_interface.state_edge["edge_next"]["http_connected"], "link_edgenext_edge_http")
    update_link_sock(param_interface.state_edge["edge_next"]["sock_connected"], "link_edgenext_edge_sock")

    # cloud_car
    update_link_con(param_interface.state_edge["cloud_car"]["http_connected"], "link_va_hu")

    # AI
    update_link_con(param_interface.state_edge["component_ai"]["http_connected"], "link_ai_edge_http")

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

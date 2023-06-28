#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_color

import dearpygui.dearpygui as dpg


# Main function
def update_color_train():
    # Lidars
    update_link_socket(param_interface.state_edge["module_capture"]["sock_l1_connected"], "link_capture_edge_l1_sock")
    update_link_socket(param_interface.state_edge["module_capture"]["sock_l2_connected"], "link_capture_edge_l2_sock")

    # module_capture
    update_link_socket(param_interface.state_capture["lidar_1"]["connected"] and param_interface.state_capture["lidar_1"]["activated"], "link_l1_py")
    update_link_socket(param_interface.state_capture["lidar_2"]["connected"] and param_interface.state_capture["lidar_2"]["activated"], "link_l2_py")
def update_color_edge_1():
    # Inter Edge
    update_link_connection(param_interface.state_edge["train_operator"]["broker_connected"], "link_edge_trainope_mqtt")
    update_link_connection(param_interface.state_edge["module_capture"]["http_connected"], "link_edge_capture_http")
    #update_link_connection(param_interface.state_edge["edge_next"]["http_connected"], "link_edge_edge_2_http")
    #update_link_socket(param_interface.state_edge["edge_next"]["sock_connected"], "link_edge_edge_2_sock")
    update_link_socket(param_interface.state_edge["component_process"]["sock_connected"], "link_edge_processing_sock")
    update_link_connection(param_interface.state_edge["component_process"]["http_connected"], "link_edge_processing_http")
    update_link_connection(param_interface.state_edge["component_ai"]["http_connected"], "link_ai_edge_1_http")

    # Edge <-> Interface
    update_link_connection(param_interface.state_interface["edge"]["http_connected"], "link_interface_edge_1_http")
    update_link_connection(param_interface.state_interface["ssd"]["connected"], "link_interface_ssd")
    update_link_socket(param_interface.state_interface["edge"]["sock_l1_connected"], "link_edge_interface_l1_sock")
    update_link_socket(param_interface.state_interface["edge"]["sock_l2_connected"], "link_edge_interface_l2_sock")

    # Edge <-> Cloud
    update_link_connection(param_interface.state_edge["cloud_car"]["http_connected"], "link_va_hu")

# Subfunction
def update_link_connection(state, tag):
    if(state):
        conn = scheme_color.color_link_green()
        dpg.bind_item_theme(tag, conn)
    else:
        disconn = scheme_color.color_link_red()
        dpg.bind_item_theme(tag, disconn)
def update_link_socket(state, tag):
    if(state):
        conn = scheme_color.color_link_blue()
        dpg.bind_item_theme(tag, conn)
    else:
        disconn = scheme_color.color_link_whiteblue()
        dpg.bind_item_theme(tag, disconn)

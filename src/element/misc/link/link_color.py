#---------------------------------------------
from src.param import param_control
from src.gui.style import gui_color
import dearpygui.dearpygui as dpg


# Main function
def update_color_train():
    pass
    # Lidars
    #update_link_socket(param_control.state_edge["module_capture"]["sock_l1_connected"], "link_edge_1_capture_l1_sock")
    #update_link_socket(param_control.state_edge["module_capture"]["sock_l2_connected"], "link_edge_1_capture_l2_sock")
    #update_link_connection(param_control.state_control["ssd"]["connected"], "link_control_ssd_usb")

    # Capture
    #update_link_socket(param_control.state_capture["lidar_1"]["connected"] and param_control.state_capture["lidar_1"]["activated"], "link_l1_py")
    #update_link_socket(param_control.state_capture["lidar_2"]["connected"] and param_control.state_capture["lidar_2"]["activated"], "link_l2_py")

def update_color_edge_1():
    # Inter Edge
    update_link_socket(param_control.state_edge["slam"]["sock_connected"], "link_edge_1_processing_sock")
    update_link_connection(param_control.state_edge["slam"]["http_connected"], "link_edge_1_processing_http")
    update_link_connection(param_control.state_edge["ai"]["http_connected"], "link_edge_1_ai_http")

    # Edge <-> Control
    update_link_connection(param_control.state_control["edge"]["http_connected"], "link_edge_1_control_http")
    update_link_socket(param_control.state_control["edge"]["sock_l1_connected"], "link_edge_1_interface_l1_sock")
    update_link_socket(param_control.state_control["edge"]["sock_l2_connected"], "link_edge_1_interface_l2_sock")

    # Edge <-> Capture
    update_link_connection(param_control.state_edge["module_capture"]["http_connected"], "link_edge_1_capture_http")

    # Edge <-> Cloud
    update_link_connection(param_control.state_edge["cloud_operator"]["broker_connected"], "link_edge_1_trainope_mqtt")
    update_link_connection(param_control.state_edge["cloud_car"]["http_connected"], "link_edge_1_car_http")

def update_color_edge_2():
    # Inter Edge
    update_link_socket(param_control.state_edge_2["slam"]["sock_connected"], "link_edge_2_processing_sock")
    update_link_connection(param_control.state_edge_2["slam"]["http_connected"], "link_edge_2_processing_http")
    update_link_connection(param_control.state_edge_2["ai"]["http_connected"], "link_edge_2_ai_http")
    
    # Edge <-> Capture
    update_link_connection(param_control.state_edge_2["module_capture"]["http_connected"], "link_edge_2_capture_http")

    # Edge <-> Cloud
    update_link_connection(param_control.state_edge_2["cloud_operator"]["broker_connected"], "link_edge_2_trainope_mqtt")
    update_link_connection(param_control.state_edge_2["cloud_car"]["http_connected"], "link_edge_2_car_http")

#---------------------------------------------
from src.param import param_interface
from src.connection.HTTPS import https_client_get
from src.connection.HTTPS import https_client_post
from src.connection.SOCK import sock_server

import dearpygui.dearpygui as dpg


def callback_module_edge():
    l1_port = dpg.get_value("edge_sock_server_l1_port")
    l2_port = dpg.get_value("edge_sock_server_l2_port")
    if(l1_port != l2_port):
        param_interface.state_edge["self"]["sock_server_l1_port"] = l1_port
        param_interface.state_edge["self"]["sock_server_l2_port"] = l2_port
        https_client_post.post_state("edge", param_interface.state_edge)

def callback_trainope():
    param_interface.state_edge["train_operator"]["broker_port"] = dpg.get_value("trainope_broker_port")
    param_interface.state_edge["train_operator"]["mqtt_topic"] = dpg.get_value("trainope_mqtt_topic")
    param_interface.state_edge["train_operator"]["mqtt_client"] = dpg.get_value("edge_mqtt_client_name")
    https_client_post.post_state("edge", param_interface.state_edge)
    https_client_post.post_param_value("edge", None, "train_operator", "reset")

def callback_module_interface():
    l1_port = dpg.get_value("interface_sock_server_l1_port")
    l2_port = dpg.get_value("interface_sock_server_l2_port")
    if(l1_port != l2_port):
        param_interface.state_interface["self"]["sock_server_l1_port"] = l1_port
        param_interface.state_interface["self"]["sock_server_l2_port"] = l2_port
        sock_server.restart_daemon()

        param_interface.state_edge["module_interface"]["sock_server_l1_port"] = dpg.get_value("interface_sock_server_l1_port")
        param_interface.state_edge["module_interface"]["sock_server_l2_port"] = dpg.get_value("interface_sock_server_l2_port")
        https_client_post.post_state("edge", param_interface.state_edge)

def callback_module_capture():
    param_interface.state_capture["lidar_1"]["activated"] = dpg.get_value("l1_activated")
    param_interface.state_capture["lidar_1"]["ip"] = dpg.get_value("l1_ip")
    param_interface.state_capture["lidar_1"]["device"] = dpg.get_value("capture_l1_device")
    param_interface.state_capture["lidar_2"]["activated"] = dpg.get_value("l2_activated")
    param_interface.state_capture["lidar_2"]["ip"] = dpg.get_value("l2_ip")
    param_interface.state_capture["lidar_2"]["speed"] = dpg.get_value("l2_speed")
    param_interface.state_capture["lidar_2"]["device"] = dpg.get_value("capture_l2_device")
    https_client_post.post_state("capture", param_interface.state_capture)

def callback_component_process():
    https_client_post.post_param_value("ve", None, "slam", dpg.get_value("processing_opt_slam"))
    https_client_post.post_param_value("ve", None, "view", dpg.get_value("processing_opt_view"))

def callback_component_process_reset():
    https_client_post.post_param_value("ve", None, None, "reset")

def callback_ai():
    https_client_post.post_param_value("component_ai", None, "lidar_height", dpg.get_value("ai_lidar_height"))
    https_client_post.post_param_value("component_ai", None, "threshold", dpg.get_value("ai_threshold"))

def callback_ssd():
    param_interface.path_ssd = dpg.get_value("ssd_path")
    param_interface.state_interface["ssd"]["activated"] = dpg.get_value("ssd_active")

def callback_lidar():
    param_interface.state_capture["lidar_1"]["port"] = dpg.get_value("l1_port")
    param_interface.state_capture["lidar_2"]["port"] = dpg.get_value("l2_port")
    https_client_post.post_state("capture", param_interface.state_capture)

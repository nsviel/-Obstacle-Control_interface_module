#---------------------------------------------
from src.param import param_interface
from src.connection.HTTPS import https_client_get
from src.connection.HTTPS import https_client_post
from src import loop

import dearpygui.dearpygui as dpg


def callback_module_edge():
    l1_port = dpg.get_value(object.object.edge_1.ID_sock_server_l1_port)
    l2_port = dpg.get_value(object.object.edge_1.ID_sock_server_l2_port)
    if(l1_port != l2_port):
        param_interface.state_edge_1["self"]["sock_server_l1_port"] = l1_port
        param_interface.state_edge_1["self"]["sock_server_l2_port"] = l2_port
        https_client_post.post_state("edge", param_interface.state_edge_1)

def callback_trainope():
    param_interface.state_edge_1["cloud_operator"]["broker_port"] = dpg.get_value(object.object.operator.ID_mqtt_broker_port)
    param_interface.state_edge_1["cloud_operator"]["mqtt_topic"] = dpg.get_value(object.object.operator.ID_mqtt_topic)
    param_interface.state_edge_1["cloud_operator"]["mqtt_client"] = dpg.get_value(object.object.edge_1.ID_mqtt_client_name)
    https_client_post.post_state("edge", param_interface.state_edge_1)
    https_client_post.post_param_value("edge", None, "cloud_operator", "reset")

def callback_module_interface():
    l1_port = dpg.get_value(object.object.control.ID_sock_server_l1_port)
    l2_port = dpg.get_value(object.object.control.ID_sock_server_l2_port)
    if(l1_port != l2_port):
        param_interface.state_control["self"]["sock_server_l1_port"] = l1_port
        param_interface.state_control["self"]["sock_server_l2_port"] = l2_port
        loop.daemon_socket_l1.restart_daemon()
        loop.daemon_socket_l2.restart_daemon()

        param_interface.state_edge_1["module_interface"]["sock_server_l1_port"] = dpg.get_value(object.object.control.ID_sock_server_l1_port)
        param_interface.state_edge_1["module_interface"]["sock_server_l2_port"] = dpg.get_value(object.object.control.ID_sock_server_l2_port)
        https_client_post.post_state("edge", param_interface.state_edge_1)

def callback_module_capture():
    param_interface.state_capture["lidar_1"]["activated"] = dpg.get_value(object.object.train.ID_l1_activated)
    param_interface.state_capture["lidar_1"]["ip"] = dpg.get_value(object.object.train.ID_l1_ip)
    param_interface.state_capture["lidar_1"]["device"] = dpg.get_value(object.object.capture.ID_device_l1)
    param_interface.state_capture["lidar_2"]["activated"] = dpg.get_value(object.object.train.ID_l2_activated)
    param_interface.state_capture["lidar_2"]["ip"] = dpg.get_value(object.object.train.ID_l2_ip)
    param_interface.state_capture["lidar_2"]["speed"] = dpg.get_value(object.object.train.ID_l2_motor_speed)
    param_interface.state_capture["lidar_2"]["device"] = dpg.get_value(object.object.capture.ID_device_l2)
    https_client_post.post_state("capture", param_interface.state_capture)

def callback_component_process():
    https_client_post.post_param_value("ve", None, "slam", dpg.get_value(object.object.edge_1.slam.ID_setting_with_slam))
    https_client_post.post_param_value("ve", None, "view", dpg.get_value(object.object.edge_1.slam.ID_setting_cam_view))

def callback_component_process_reset():
    https_client_post.post_param_value("ve", None, None, "reset")

def callback_ai():
    https_client_post.post_param_value("component_ai", None, "lidar_height", dpg.get_value(object.object.edge_1.ai.ID_setting_lidar_height))
    https_client_post.post_param_value("component_ai", None, "threshold", dpg.get_value(object.object.edge_1.ai.ID_setting_threshold))

def callback_ssd():
    param_interface.path_ssd = dpg.get_value(object.object.ssd.ID_path)
    param_interface.state_control["ssd"]["activated"] = dpg.get_value(object.object.ssd.ID_activated)

def callback_lidar():
    param_interface.state_capture["lidar_1"]["port"] = dpg.get_value(object.object.train.ID_l1_sock_client_port)
    param_interface.state_capture["lidar_2"]["port"] = dpg.get_value(object.object.train.ID_l2_sock_client_port)
    https_client_post.post_state("capture", param_interface.state_capture)

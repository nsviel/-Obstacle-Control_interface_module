#---------------------------------------------
from src.param import param_co
from src.HTTPS import https_client_get
from src.HTTPS import https_client_post
from src.SOCK import sock_server

import dearpygui.dearpygui as dpg


def callback_hubium():
    l1_port = dpg.get_value("hu_sock_server_l1_port")
    l2_port = dpg.get_value("hu_sock_server_l2_port")
    if(l1_port != l2_port):
        param_co.state_hu["self"]["sock_server_l1_port"] = l1_port
        param_co.state_hu["self"]["sock_server_l2_port"] = l2_port
        https_client_post.post_state("hu", param_co.state_hu)

def callback_sncf():
    param_co.state_hu["sncf"]["broker_port"] = dpg.get_value("sncf_broker_port")
    param_co.state_hu["sncf"]["mqtt_topic"] = dpg.get_value("sncf_mqtt_topic")
    param_co.state_hu["sncf"]["mqtt_client"] = dpg.get_value("hu_mqtt_client_name")
    https_client_post.post_state("hu", param_co.state_hu)
    https_client_post.post_param_value("hu", None, "sncf", "reset")

def callback_controlium():
    l1_port = dpg.get_value("co_sock_server_l1_port")
    l2_port = dpg.get_value("co_sock_server_l2_port")
    if(l1_port != l2_port):
        param_co.state_co["self"]["sock_server_l1_port"] = l1_port
        param_co.state_co["self"]["sock_server_l2_port"] = l2_port
        sock_server.restart_daemon()

        param_co.state_hu["controlium"]["sock_server_l1_port"] = dpg.get_value("co_sock_server_l1_port")
        param_co.state_hu["controlium"]["sock_server_l2_port"] = dpg.get_value("co_sock_server_l2_port")
        https_client_post.post_state("hu", param_co.state_hu)

def callback_pywardium():
    param_co.state_py["lidar_1"]["activated"] = dpg.get_value("l1_activated")
    param_co.state_py["lidar_1"]["ip"] = dpg.get_value("l1_ip")
    param_co.state_py["lidar_1"]["speed"] = dpg.get_value("l1_speed")
    param_co.state_py["lidar_1"]["device"] = dpg.get_value("py_l1_device")
    param_co.state_py["lidar_2"]["activated"] = dpg.get_value("l2_activated")
    param_co.state_py["lidar_2"]["ip"] = dpg.get_value("l2_ip")
    param_co.state_py["lidar_2"]["speed"] = dpg.get_value("l2_speed")
    param_co.state_py["lidar_2"]["device"] = dpg.get_value("py_l2_device")
    https_client_post.post_state("py", param_co.state_py)

def callback_velodium():
    https_client_post.post_param_value("ve", None, "slam", dpg.get_value("ve_opt_slam"))
    https_client_post.post_param_value("ve", None, "view", dpg.get_value("ve_opt_view"))

def callback_velodium_reset():
    https_client_post.post_param_value("ve", None, None, "reset")

def callback_ai():
    https_client_post.post_param_value("ai", None, "lidar_height", dpg.get_value("ai_lidar_height"))
    https_client_post.post_param_value("ai", None, "threshold", dpg.get_value("ai_threshold"))

def callback_ssd():
    param_co.path_ssd = dpg.get_value("ssd_path")
    param_co.state_co["ssd"]["activated"] = dpg.get_value("ssd_active")

def callback_lidar():
    param_co.state_py["lidar_1"]["port"] = dpg.get_value("l1_port")
    param_co.state_py["lidar_2"]["port"] = dpg.get_value("l2_port")
    https_client_post.post_state("py", param_co.state_py)

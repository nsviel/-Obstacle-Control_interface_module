#---------------------------------------------
from src.param import param_interface
from src.connection.HTTPS import https_client_get
from src.connection.HTTPS import https_client_post
from src.connection.HTTPS import https_client_con
from src.connection.SOCK import sock_server
from src.misc import saving
from src.misc import wallet

import dearpygui.dearpygui as dpg


def command_false_alarm():
    print("[\033[1;32mOK\033[0m] Send false alarm")
    https_client_post.post_param_value("edge", None, "train_operator", "false_alarm")

def command_new_save():
    saving.determine_path()

def command_ssd_editing():
    param_interface.state_interface["path"]["file_name_add"] = dpg.get_value("ssd_path_add")
    param_interface.path_ssd = dpg.get_value("ssd_path")
    saving.determine_path()

def command_comboip():
    edge_1_ip = wallet.get_ip_from_key(dpg.get_value("edge_1_wallet"))
    capture_ip = wallet.get_ip_from_key(dpg.get_value("capture_wallet"))
    edge_2_ip = wallet.get_ip_from_key(dpg.get_value("edge_2_wallet"))
    processing_ip = wallet.get_ip_from_key(dpg.get_value("processing_wallet"))
    ai_ip = wallet.get_ip_from_key(dpg.get_value("ai_wallet"))
    ip_operator = wallet.get_ip_from_key(dpg.get_value("trainope_wallet"))
    l1_ip = wallet.get_ip_from_key(dpg.get_value("l1_wallet"))
    l2_ip = wallet.get_ip_from_key(dpg.get_value("l2_wallet"))

    if(edge_1_ip != None):
        param_interface.state_interface["edge"]["ip"] = edge_1_ip
        dpg.set_value("edge_1_ip", edge_1_ip)
        https_client_con.test_edge_con()
        https_client_post.post_param_value("capture", "edge", "ip", edge_1_ip)
    if(capture_ip != None):
        param_interface.state_edge["module_capture"]["ip"] = capture_ip
        dpg.set_value("capture_ip", capture_ip)
        https_client_post.post_param_value("edge", "module_capture", "ip", capture_ip)
    if(edge_2_ip != None):
        param_interface.state_edge["edge_next"]["ip"] = edge_2_ip
        dpg.set_value("edge_2_ip", edge_2_ip)
        https_client_post.post_param_value("edge", "edge_next", "ip", edge_2_ip)
    if(processing_ip != None):
        param_interface.state_edge["component_process"]["ip"] = processing_ip
        dpg.set_value("edge_2_ip", processing_ip)
        https_client_post.post_param_value("edge", "component_process", "ip", processing_ip)
    if(ai_ip != None):
        param_interface.state_edge["component_ai"]["ip"] = ai_ip
        dpg.set_value("ai_ip", ai_ip)
        https_client_post.post_param_value("edge", "component_ai", "ip", ai_ip)
    if(ip_operator != None):
        param_interface.state_edge["train_operator"]["broker_ip"] = ip_operator
        dpg.set_value("ip_operator", ip_operator)
        https_client_post.post_param_value("edge", "train_operator", "broker_ip", ip_operator)
    if(l1_ip != None):
        param_interface.state_capture["lidar_1"]["ip"] = l1_ip
        dpg.set_value("l1_ip", l1_ip)
        https_client_post.post_param_value("capture", "lidar_1", "ip", l1_ip)
    if(l2_ip != None):
        param_interface.state_capture["lidar_2"]["ip"] = l2_ip
        dpg.set_value("l2_ip", l2_ip)
        https_client_post.post_param_value("capture", "lidar_2", "ip", l2_ip)

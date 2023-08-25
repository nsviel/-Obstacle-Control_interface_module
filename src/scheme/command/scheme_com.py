#---------------------------------------------
from src.param import param_interface
from src.connection.HTTPS import https_client_get
from src.connection.HTTPS import https_client_post
from src.connection.HTTPS import https_client_con
from src.utils import saving
from src.utils import wallet

import dearpygui.dearpygui as dpg


def command_false_alarm():
    print("[\033[1;32mOK\033[0m] Send false alarm")
    https_client_post.post_param_value("edge", None, "cloud_operator", "false_alarm")

def command_new_save():
    saving.determine_path()

def command_ssd_editing():
    param_interface.state_control["path"]["file_name_add"] = dpg.get_value(object.object.ssd.ID_path_add)
    param_interface.path_ssd = dpg.get_value(object.object.ssd.ID_path)
    saving.determine_path()

def command_comboip():
    edge_1_ip = wallet.get_ip_from_key(dpg.get_value(object.object.edge_1.ID_wallet))
    capture_ip = wallet.get_ip_from_key(dpg.get_value(object.object.capture.ID_wallet))
    edge_2_ip = wallet.get_ip_from_key(dpg.get_value("edge_2_wallet"))
    processing_ip = wallet.get_ip_from_key(dpg.get_value(object.object.edge_1.slam.ID_wallet))
    ai_ip = wallet.get_ip_from_key(dpg.get_value(object.object.edge_1.ai.ID_wallet))
    ip_operator = wallet.get_ip_from_key(dpg.get_value(object.object.operator.ID_wallet))
    l1_ip = wallet.get_ip_from_key(dpg.get_value(object.object.train.ID_l1_wallet))
    l2_ip = wallet.get_ip_from_key(dpg.get_value(object.object.train.ID_l2_wallet))

    if(edge_1_ip != None):
        param_interface.state_control["edge_1"]["ip"] = edge_1_ip
        dpg.set_value(object.object.edge_1.ID_ip, edge_1_ip)
        https_client_con.test_edge_con()
        https_client_post.post_param_value("capture", "edge_1", "ip", edge_1_ip)
    if(capture_ip != None):
        param_interface.state_edge_1["module_capture"]["ip"] = capture_ip
        dpg.set_value(object.object.capture.ID_ip, capture_ip)
        https_client_post.post_param_value("edge", "module_capture", "ip", capture_ip)
    if(edge_2_ip != None):
        param_interface.state_edge_2["edge"]["ip"] = edge_2_ip
        dpg.set_value("edge_2_ip", edge_2_ip)
        https_client_post.post_param_value("edge", "edge_2", "ip", edge_2_ip)
    if(processing_ip != None):
        param_interface.state_edge_1["component_process"]["ip"] = processing_ip
        dpg.set_value("edge_2_ip", processing_ip)
        https_client_post.post_param_value("edge", "component_process", "ip", processing_ip)
    if(ai_ip != None):
        param_interface.state_edge_1["component_ai"]["ip"] = ai_ip
        dpg.set_value(object.object.edge_1.ai.ID_ip, ai_ip)
        https_client_post.post_param_value("edge", "component_ai", "ip", ai_ip)
    if(ip_operator != None):
        param_interface.state_edge_1["cloud_operator"]["broker_ip"] = ip_operator
        dpg.set_value(object.object.operator.ID_ip, ip_operator)
        https_client_post.post_param_value("edge", "cloud_operator", "broker_ip", ip_operator)
    if(l1_ip != None):
        param_interface.state_capture["lidar_1"]["ip"] = l1_ip
        dpg.set_value(object.object.train.ID_l1_ip, l1_ip)
        https_client_post.post_param_value("capture", "lidar_1", "ip", l1_ip)
    if(l2_ip != None):
        param_interface.state_capture["lidar_2"]["ip"] = l2_ip
        dpg.set_value(object.object.train.ID_l2_ip, l2_ip)
        https_client_post.post_param_value("capture", "lidar_2", "ip", l2_ip)

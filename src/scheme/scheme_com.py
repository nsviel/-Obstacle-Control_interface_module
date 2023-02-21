#---------------------------------------------
from src.param import param_co
from src.HTTPS import https_client_get
from src.HTTPS import https_client_post
from src.HTTPS import https_client_con
from src.SOCK import sock_server
from src.misc import saving
from src.misc import wallet

import dearpygui.dearpygui as dpg


def command_false_alarm():
    print("[\033[1;32mOK\033[0m] Send false alarm")
    https_client_post.post_param_value("hu", None, "train_operator", "false_alarm")

def command_new_save():
    saving.determine_path()

def command_ssd_editing():
    param_co.state_co["path"]["file_name_add"] = dpg.get_value("ssd_path_add")
    param_co.path_ssd = dpg.get_value("ssd_path")
    saving.determine_path()

def command_comboip():
    hu_ip = wallet.get_ip_from_key(dpg.get_value("hu_wallet"))
    py_ip = wallet.get_ip_from_key(dpg.get_value("py_wallet"))
    ed_ip = wallet.get_ip_from_key(dpg.get_value("ed_wallet"))
    ve_ip = wallet.get_ip_from_key(dpg.get_value("ve_wallet"))
    ai_ip = wallet.get_ip_from_key(dpg.get_value("ai_wallet"))
    ip_operator = wallet.get_ip_from_key(dpg.get_value("sncf_wallet"))
    l1_ip = wallet.get_ip_from_key(dpg.get_value("l1_wallet"))
    l2_ip = wallet.get_ip_from_key(dpg.get_value("l2_wallet"))

    if(hu_ip != None):
        param_co.state_co["module_edge"]["ip"] = hu_ip
        dpg.set_value("hu_ip", hu_ip)
        https_client_con.test_hu_con()
        https_client_post.post_param_value("py", "module_edge", "ip", hu_ip)
    if(py_ip != None):
        param_co.state_hu["module_capture"]["ip"] = py_ip
        dpg.set_value("py_ip", py_ip)
        https_client_post.post_param_value("hu", "module_capture", "ip", py_ip)
    if(ed_ip != None):
        param_co.state_hu["edge_next"]["ip"] = ed_ip
        dpg.set_value("ed_ip", ed_ip)
        https_client_post.post_param_value("hu", "edge_next", "ip", ed_ip)
    if(ve_ip != None):
        param_co.state_hu["component_process"]["ip"] = ve_ip
        dpg.set_value("ed_ip", ve_ip)
        https_client_post.post_param_value("hu", "component_process", "ip", ve_ip)
    if(ai_ip != None):
        param_co.state_hu["component_ai"]["ip"] = ai_ip
        dpg.set_value("ai_ip", ai_ip)
        https_client_post.post_param_value("hu", "component_ai", "ip", ai_ip)
    if(ip_operator != None):
        param_co.state_hu["train_operator"]["broker_ip"] = ip_operator
        dpg.set_value("ip_operator", ip_operator)
        https_client_post.post_param_value("hu", "train_operator", "broker_ip", ip_operator)
    if(l1_ip != None):
        param_co.state_py["lidar_1"]["ip"] = l1_ip
        dpg.set_value("l1_ip", l1_ip)
        https_client_post.post_param_value("py", "lidar_1", "ip", l1_ip)
    if(l2_ip != None):
        param_co.state_py["lidar_2"]["ip"] = l2_ip
        dpg.set_value("l2_ip", l2_ip)
        https_client_post.post_param_value("py", "lidar_2", "ip", l2_ip)

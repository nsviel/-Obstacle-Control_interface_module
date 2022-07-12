#! /usr/bin/python
#---------------------------------------------

from param import param_co

from src import saving
from src import http_client_get

import dearpygui.dearpygui as dpg


def callback_update_conf():
    a=1

def callback_lidar():
    param_co.state_co["lidar_1"]["speed"] = dpg.get_value("l1_speed")
    param_co.state_co["lidar_2"]["speed"] = dpg.get_value("l2_speed")
    param_co.state_co["lidar_1"]["ip"] = dpg.get_value("l1_ip")
    param_co.state_co["lidar_2"]["ip"] = dpg.get_value("l2_ip")

def callback_false_alarm():
    http_client_get.get_falsealarm()

def callback_ssd():
    param_co.path_ssd = dpg.get_value("ssd_path")
    param_co.state_co["ssd"]["activated"] = dpg.get_value("ssd_active")
    param_co.state_py["path"]["additional"] = dpg.get_value("ssd_path_add")
    saving.determine_path()

def callback_choice_device():
    param_co.state_co["lidar_1"]["device"] = str(dpg.get_value("py_l1_device"))
    param_co.state_co["lidar_2"]["device"] = str(dpg.get_value("py_l2_device"))

def callback_comboip():
    adress = dpg.get_value("comboip")
    for i in range(0, len(param_py.wallet_add)):
        if(adress == param_py.wallet_add[i]):
            param_hu.ip = param_py.wallet_ip[i]
    dpg.set_value("hubiump", param_hu.ip)

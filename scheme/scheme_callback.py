#! /usr/bin/python
#---------------------------------------------

from param import param_co
from param import param_li

from src import http_get

import dearpygui.dearpygui as dpg


def callback_lidar():
    param_li.with_two_lidar = dpg.get_value("cwtl")
    param_li.with_writing = dpg.get_value("cwws")
    param_li.l1_speed = dpg.get_value("l1_speed")
    param_li.l2_speed = dpg.get_value("l2_speed")
    param_li.l1_ip = dpg.get_value("l1_ip")
    param_li.l2_ip = dpg.get_value("l2_ip")

def callback_false_alarm():
    http_get.get_falsealarm()

def callback_ssd():
    param_co.ssd_path = dpg.get_value("ssd_path")
    param_li.path_name = dpg.get_value("ssd_path_add")

def callback_choice_device():
    param_li.device_l1 = str(dpg.get_value("l1d"))
    param_li.device_l2 = str(dpg.get_value("l2d"))

def callback_comboip():
    adress = dpg.get_value("comboip")
    for i in range(0, len(param_py.wallet_add)):
        if(adress == param_py.wallet_add[i]):
            param_hu.ip = param_py.wallet_ip[i]
    dpg.set_value("hubiump", param_hu.ip)

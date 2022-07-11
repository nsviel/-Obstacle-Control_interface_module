#! /usr/bin/python
#---------------------------------------------

from param import param_co
from classes import classes

from src import saving
from src import http_get

import dearpygui.dearpygui as dpg


def callback_update_conf():
    a=1

def callback_lidar():
    classes.lidars.l1_speed = dpg.get_value("l1_speed")
    classes.lidars.l2_speed = dpg.get_value("l2_speed")
    classes.lidars.l1_ip = dpg.get_value("l1_ip")
    classes.lidars.l2_ip = dpg.get_value("l2_ip")

def callback_false_alarm():
    http_get.get_falsealarm()

def callback_ssd():
    param_co.ssd_path = dpg.get_value("ssd_path")
    param_co.ssd_activated = dpg.get_value("ssd_active")
    classes.lidars.path_add = dpg.get_value("ssd_path_add")
    saving.determine_path()

def callback_choice_device():
    classes.lidars.device_l1 = str(dpg.get_value("py_l1_device"))
    classes.lidars.device_l2 = str(dpg.get_value("py_l2_device"))

def callback_comboip():
    adress = dpg.get_value("comboip")
    for i in range(0, len(param_py.wallet_add)):
        if(adress == param_py.wallet_add[i]):
            param_hu.ip = param_py.wallet_ip[i]
    dpg.set_value("hubiump", param_hu.ip)

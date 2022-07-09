#! /usr/bin/python
#---------------------------------------------

from param import param_py
from param import param_hu
from param import param_li

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def callback_parameter():
    param_li.with_two_lidar = dpg.get_value("cwtl")
    param_li.with_writing = dpg.get_value("cwws")
    param_li.lidar_speed = dpg.get_value("ls")

    param_hu.ip = dpg.get_value("hubiump")
    param_hu.sock_server_port = dpg.get_value("hubiumpos")
    param_hu.http_server_port = dpg.get_value("hubiumpoh")

    param_li.ip_l1 = dpg.get_value("l1ip")
    param_li.ip_l2 = dpg.get_value("l2ip")

def callback_demo():
    is_demo = dpg.get_value("demo")
    if(is_demo):
        demo.show_demo()

def callback_connection():
    if(param_py.http_connected):
        dpg.set_value("httpconn", "ON")
    else:
        dpg.set_value("httpconn", "OFF")
    if(param_py.socket_connected):
        dpg.set_value("socketconn", "ON")
    else:
        dpg.set_value("socketconn", "OFF")

def callback_close():
    param_py.run_loop = dpg.get_value("bclo")

def callback_path():
    param_py.ssd_path = dpg.get_value("ssdp")
    param_li.path_name = dpg.get_value("pnam")

def callback_choice_device():
    param_li.device_l1 = str(dpg.get_value("l1d"))
    param_li.device_l2 = str(dpg.get_value("l2d"))

def callback_refresh_device():
    devices = 1

def callback_comboip():
    adress = dpg.get_value("comboip")
    for i in range(0, len(param_py.wallet_add)):
        if(adress == param_py.wallet_add[i]):
            param_hu.ip = param_py.wallet_ip[i]
    dpg.set_value("hubiump", param_hu.ip)

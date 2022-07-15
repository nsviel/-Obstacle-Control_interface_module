#! /usr/bin/python
#---------------------------------------------

from param import param_co
from conn import http_client_get

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def callback_demo():
    demo.show_demo()

def callback_close():
    param_co.run_loop = False

def callback_test():
    http_client_get.get_image()

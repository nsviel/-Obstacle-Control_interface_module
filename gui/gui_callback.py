#! /usr/bin/python
#---------------------------------------------

from param import classes
from src import http_get

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def callback_demo():
    demo.show_demo()

def callback_close():
    classes.contro.run_loop = False

def callback_test():
    http_get.get_image()
    pass

#! /usr/bin/python
#---------------------------------------------

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def callback_demo():
    demo.show_demo()

def callback_close():
    param_co.run_loop = False

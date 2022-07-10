#! /usr/bin/python
#---------------------------------------------

from param import param_li

import dearpygui.dearpygui as dpg


def loop():
    loop_packet()

def loop_packet():
    dpg.set_value("l1_packet", param_li.l1_nb_packet)
    dpg.set_value("l2_packet", param_li.l2_nb_packet)

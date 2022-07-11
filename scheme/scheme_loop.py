#! /usr/bin/python
#---------------------------------------------

from param import cla

import dearpygui.dearpygui as dpg


def loop():
    loop_packet()

def loop_packet():
    dpg.set_value("l1_packet", cla.lidars.l1_nb_packet)
    dpg.set_value("l2_packet", cla.lidars.l2_nb_packet)

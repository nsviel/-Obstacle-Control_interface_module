#! /usr/bin/python
#---------------------------------------------

from classes import classes

import dearpygui.dearpygui as dpg


def loop():
    loop_packet()

def loop_packet():
    dpg.set_value("l1_packet", classes.lidars.l1_nb_packet)
    dpg.set_value("l2_packet", classes.lidars.l2_nb_packet)

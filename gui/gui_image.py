#! /usr/bin/python
#---------------------------------------------

from param import cla

import dearpygui.dearpygui as dpg


def init_image():
    width, height, channels, data = dpg.load_image("state/image")

    with dpg.texture_registry():
        dpg.add_dynamic_texture(width, height, data, tag="image_in")

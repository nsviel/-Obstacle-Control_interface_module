#! /usr/bin/python
#---------------------------------------------

import dearpygui.dearpygui as dpg


def init_image():
    width, height, channels, data = dpg.load_image("/home/aether/Desktop/System/Hubium/data/generic/image")

    if(width != None):
        with dpg.texture_registry():
            dpg.add_static_texture(width, height, data, tag="image_in")
    else:
        print("Error loading image !")

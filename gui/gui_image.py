#! /usr/bin/python
#---------------------------------------------

from param import param_co
import dearpygui.dearpygui as dpg


def init_image():
    try:
        width, height, channels, data = dpg.load_image(param_co.path_image)

        with dpg.texture_registry():
            dpg.add_dynamic_texture(width, height, data, tag="image_in")
    except:
        print("[error] No image !")
        exit()

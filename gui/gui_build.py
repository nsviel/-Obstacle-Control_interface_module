#! /usr/bin/python
#---------------------------------------------

from gui import gui_callback
from gui import gui_parameter
from gui import gui_runtime
from gui import scheme

import dearpygui.dearpygui as dpg


def build():
    scheme.build_scheme()
    gui_parameter.build_parameter()
    gui_runtime.build_runtime()
    build_end()

def build_end():
    dpg.add_separator()
    dpg.add_button(label="close", tag="bclo", callback=gui_callback.callback_close)
    dpg.add_checkbox(tag="demo", label="demo", default_value=False, callback=gui_callback.callback_demo);

def build_theme():
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (20, 20, 20), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)
            dpg.add_theme_color(dpg.mvThemeCol_Button, (20, 20, 20))

    dpg.bind_theme(global_theme)

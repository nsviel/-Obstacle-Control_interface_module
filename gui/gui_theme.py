#---------------------------------------------
from param import param_co
import dearpygui.dearpygui as dpg


def gui_font():
    with dpg.font_registry():
        param_co.gui_font_def = dpg.add_font("gui/font/ProggyClean.ttf", 13)
        param_co.gui_font_big = dpg.add_font("gui/font/DroidSans.ttf", 25)

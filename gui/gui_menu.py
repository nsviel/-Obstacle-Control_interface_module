#! /usr/bin/python
#---------------------------------------------

from gui import gui_callback

import dearpygui.dearpygui as dpg


def menu():
    with dpg.menu_bar():
        with dpg.menu(label="Menu"):
            dpg.add_menu_item(label="Demo", callback=gui_callback.callback_demo)
        dpg.add_button(label="Close", callback=gui_callback.callback_close)

#---------------------------------------------
from param import param_co
from gui import gui_callback

import dearpygui.dearpygui as dpg


def menu():
    with dpg.menu_bar():
        with dpg.menu(label="Menu"):
            dpg.add_menu_item(label="Wallet", callback=lambda s, a, u: dpg.configure_item("win_wallet", show=True))
            with dpg.menu(label="Mode"):
                dpg.add_menu_item(label="dev", callback=gui_callback.callback_mode_dev)
                dpg.add_menu_item(label="demo", callback=gui_callback.callback_mode_demo)
            dpg.add_menu_item(label="Dearpygui", callback=gui_callback.callback_demo)
        dpg.add_button(label="Close", callback=gui_callback.callback_close)

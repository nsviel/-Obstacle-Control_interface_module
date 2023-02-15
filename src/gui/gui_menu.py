#---------------------------------------------
from src.param import param_co
from src.gui import gui_callback

import dearpygui.dearpygui as dpg


def menu():
    with dpg.menu_bar():
        with dpg.menu(label="Mode"):
            dpg.add_menu_item(label="Parametrization", callback=gui_callback.callback_mode_dev)
            dpg.add_menu_item(label="Overview", callback=gui_callback.callback_mode_demo_minimized)
            dpg.add_menu_item(label="Overview fullscreen", callback=gui_callback.callback_mode_demo_fullscreen)
        dpg.add_menu_item(label="Wallet", callback=lambda s, a, u: dpg.configure_item("win_wallet", show=True))
        dpg.add_button(label="Close", callback=gui_callback.callback_close)

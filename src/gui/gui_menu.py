#---------------------------------------------
from src.param import param_co
from src.gui import gui_callback

import dearpygui.dearpygui as dpg


def menu():
    with dpg.menu_bar():
        with dpg.menu(label="Menu"):
            dpg.add_menu_item(label="Wallet", callback=lambda s, a, u: dpg.configure_item("win_wallet", show=True))
            with dpg.menu(label="Mode"):
                dpg.add_menu_item(label="dev", callback=gui_callback.callback_mode_dev)
                dpg.add_menu_item(label="demo minimized", callback=gui_callback.callback_mode_demo_minimized)
                dpg.add_menu_item(label="demo fullscreen", callback=gui_callback.callback_mode_demo_fullscreen)
            dpg.add_menu_item(label="Dearpygui", callback=gui_callback.callback_demo)
        dpg.add_button(label="Close", callback=gui_callback.callback_close)

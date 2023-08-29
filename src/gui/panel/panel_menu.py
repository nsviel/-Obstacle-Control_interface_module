#---------------------------------------------
from src.gui.panel import panel_demo
from src.gui.background import gui_ID
from src.element import element
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def callback_demo():
    demo.show_demo()

def callback_close():
    param_control.run_loop = False

def callback_wallet():
    element.object.misc.wallet.window.set_visible()

def menu():
    demo = panel_demo.Demo()
    with dpg.menu_bar():
        dpg.add_menu_item(label="Close", callback=callback_close)
        dpg.add_menu_item(label="Demo", callback=demo.demo)
        dpg.add_menu_item(label="Wallet", callback=callback_wallet)

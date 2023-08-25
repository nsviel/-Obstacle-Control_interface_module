#---------------------------------------------
from src.gui.interface import gui_command
from src.gui.background import gui_demo
from src.gui.background import gui_ID
from src.element import element
import dearpygui.dearpygui as dpg


def menu():
    demo = gui_demo.Demo()
    with dpg.menu_bar():
        dpg.add_button(label="Close", callback=gui_command.callback_close)
        with dpg.menu(label="Option"):
            dpg.add_menu_item(label="Demo", callback=demo.demo)
            dpg.add_checkbox(tag=gui_ID.ID_block_visibility, label="Block visibility", default_value=False, callback=element.object.misc.block.switch_visibility)
        dpg.add_menu_item(label="Wallet", callback=gui_command.callback_wallet)

#---------------------------------------------
from src.gui.interface import gui_menu
from src.gui.background import gui_ID
from src.element import element
import dearpygui.dearpygui as dpg


def build_panel():
    with dpg.child_window(tag=gui_ID.ID_panel_setting, width=250, menubar=True, border=False):
        gui_menu.menu()
        element.object.build_windows()

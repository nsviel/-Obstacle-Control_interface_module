#---------------------------------------------
from src.gui.panel import panel_menu
from src.gui.background import gui_ID
from src.element import element
from src.gui.style import gui_color
import dearpygui.dearpygui as dpg


def build_panel():
    with dpg.child_window(tag=gui_ID.ID_panel_setting, width=250, menubar=True, border=False):
        panel_menu.menu()
        element.object.build_windows()

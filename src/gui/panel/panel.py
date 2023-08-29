#---------------------------------------------
from src.gui.panel import panel_menu
from src.gui.background import gui_ID
from src.element import element
from src.gui.style import gui_color
import dearpygui.dearpygui as dpg


def callback_block():
    element.object.misc.block.switch_visibility()
    element.object.position_nodes()

def build_panel():
    with dpg.child_window(tag=gui_ID.ID_panel_setting, width=250, menubar=True, border=False):
        panel_menu.menu()
        dpg.add_checkbox(tag=gui_ID.ID_block_visibility, label="Block visibility", default_value=False, callback=callback_block)
        element.object.build_windows()

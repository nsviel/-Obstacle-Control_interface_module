#---------------------------------------------
from src.gui.interface import gui_scheme
from src.gui.style import gui_theme
from src.gui.panel import panel
from src.gui.background import gui_ID
import dearpygui.dearpygui as dpg


# GUI creation / Destruction
def initialization():
    dpg.create_context()
    gui_theme.gui_font()
    gui_theme.gui_theme()
    build_gui()
    setup_gui()
def loop():
    dpg.render_dearpygui_frame()
    return dpg.is_dearpygui_running()
def termination():
    dpg.destroy_context()

# GUI setup
def build_gui():
    with dpg.window(tag=gui_ID.ID_window, label="module_interface", no_background=True):
        with dpg.group(horizontal=True):
            panel.build_panel()
            gui_scheme.build_scheme()

def setup_gui():
    gui_width = 1650
    gui_height = 950
    dpg.create_viewport(title='module_interface', width=gui_width, height=gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(gui_ID.ID_window, True)

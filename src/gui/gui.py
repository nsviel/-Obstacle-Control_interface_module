#---------------------------------------------
from src.param import param_control
from src.gui.scheme import scheme
from src.gui.style import gui_theme
from src.gui.panel import panel
from src.gui.background import gui_ID
from src.gui.style import gui_color
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
    with dpg.window(tag=gui_ID.ID_window, no_background=True):
        with dpg.group(horizontal=True):
            panel.build_panel()
            scheme.build_scheme()

def setup_gui():
    dpg.create_viewport(title='Control Interface', width=param_control.gui_width, height=param_control.gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(gui_ID.ID_window, True)

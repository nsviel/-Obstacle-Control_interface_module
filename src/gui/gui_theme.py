#---------------------------------------------
from src.param import param_interface
import dearpygui.dearpygui as dpg


def gui_font():
    with dpg.font_registry():
        param_interface.gui_font_def = dpg.add_font("src/gui/font/ProggyClean.ttf", 13)
        param_interface.gui_font_big = dpg.add_font("src/gui/font/DroidSans.ttf", 25)

def gui_window():
    layer_window = color_window()
    dpg.bind_item_theme("node_network", layer_window)

def color_window():
    layer_cloud = dpg.add_theme()
    with dpg.theme_component(dpg.mvTheme, parent=layer_cloud):
        color = (0, 0, 0)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, color, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, color, category=dpg.mvThemeCat_Core)
    return layer_cloud

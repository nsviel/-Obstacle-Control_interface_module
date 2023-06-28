#---------------------------------------------
from src.scheme.link import scheme_link
from src.scheme.node import scheme_node
from src.scheme.style import scheme_color
from src.scheme.style import scheme_theme
from src.scheme.node.data import scheme_plot
from src.scheme.style import scheme_mode_visibility

import dearpygui.dearpygui as dpg


def build_scheme():
    create_scheme()
    scheme_theme.colorize()
    scheme_plot.init_plot()

def create_scheme():
    # Construct node editor
    with dpg.node_editor(tag="node_editor", minimap=True, minimap_location=dpg.mvNodeMiniMap_Location_TopRight):
        scheme_node.create_node()
        scheme_link.create_link()

    with dpg.handler_registry(show=False, tag="__demo_mouse_handler"):
        m_wheel = dpg.add_mouse_wheel_handler()
        m_click = dpg.add_mouse_click_handler(button=dpg.mvMouseButton_Left)
        m_double_click = dpg.add_mouse_double_click_handler(button=dpg.mvMouseButton_Left)
        m_release = dpg.add_mouse_release_handler(button=dpg.mvMouseButton_Left)
        m_drag = dpg.add_mouse_drag_handler(button=dpg.mvMouseButton_Left)
        m_down = dpg.add_mouse_down_handler(button=dpg.mvMouseButton_Left)
        m_move = dpg.add_mouse_move_handler()

    dpg.configure_item("node_editor", show=False)

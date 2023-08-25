#---------------------------------------------
from src.element import element
from src.gui.style import gui_color
from src.gui.style import colorization
from src.gui.background import gui_ID
from src.gui.background import texture
import dearpygui.dearpygui as dpg


def build_scheme():
    with dpg.child_window(tag=gui_ID.ID_panel_scheme, border=False):
        with dpg.node_editor(tag=gui_ID.ID_scheme, minimap=True, minimap_location=dpg.mvNodeMiniMap_Location_TopRight):
            element.object.build_nodes()
            element.object.setup_handlers()
            element.object.setup_links()

    # Mouse interaction
    with dpg.handler_registry(show=False, tag=gui_ID.ID_scheme_mouse):
        m_wheel = dpg.add_mouse_wheel_handler()
        m_click = dpg.add_mouse_click_handler(button=dpg.mvMouseButton_Left)
        m_double_click = dpg.add_mouse_double_click_handler(button=dpg.mvMouseButton_Left)
        m_release = dpg.add_mouse_release_handler(button=dpg.mvMouseButton_Left)
        m_drag = dpg.add_mouse_drag_handler(button=dpg.mvMouseButton_Left)
        m_down = dpg.add_mouse_down_handler(button=dpg.mvMouseButton_Left)
        m_move = dpg.add_mouse_move_handler()

    #dpg.configure_item(gui_ID.ID_scheme, show=False)

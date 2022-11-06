#---------------------------------------------
from scheme import scheme_link
from scheme import scheme_node
from scheme import scheme_color
from scheme import scheme_theme
from scheme import scheme_plot
from scheme import scheme_visibility

import dearpygui.dearpygui as dpg


def build_scheme():
    create_scheme()
    scheme_theme.colorize()
    scheme_plot.init_plot()

def create_scheme():
    # Construct node editor
    with dpg.node_editor(tag="node_editor", minimap=True, minimap_location=dpg.mvNodeMiniMap_Location_BottomRight):
        scheme_node.node_controlium()
        scheme_node.node_pywardium()
        scheme_node.node_hubium()
        scheme_node.node_train()
        scheme_node.node_edge()
        scheme_node.node_ve()
        scheme_node.node_ai()
        scheme_node.node_sncf()
        scheme_node.node_valeo()
        scheme_node.node_ssd()
        scheme_node.node_data()
        scheme_node.node_stats()
        scheme_node.node_legend()
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

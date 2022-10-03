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
    with dpg.node_editor():
        scheme_node.node_controlium()
        scheme_node.node_pywardium()
        scheme_node.node_hubium()
        scheme_node.node_train()
        scheme_node.node_edge()
        scheme_node.node_velodium()
        scheme_node.node_ai()
        scheme_node.node_sncf()
        scheme_node.node_valeo()
        scheme_node.node_ssd()
        scheme_node.node_data()
        scheme_node.node_stats()
        scheme_link.create_link()
    # Set scheme visibility
    scheme_visibility.set_mode()

#! /usr/bin/python
#---------------------------------------------

from scheme import scheme_link
from scheme import scheme_node
from scheme import scheme_color
from scheme import scheme_theme

import dearpygui.dearpygui as dpg


def build_scheme():
    create_scheme()
    scheme_theme.colorize()

def create_scheme():
    # Construct node editor
    with dpg.node_editor():
        scheme_node.node_controlium()
        scheme_node.node_pywardium()
        scheme_node.node_hubium()
        scheme_node.node_train()
        scheme_node.node_edge()
        scheme_node.node_edge_local()
        scheme_node.node_sncf()
        scheme_node.node_valeo()
        scheme_node.node_ssd()
        scheme_node.node_data()
        scheme_link.create_link()

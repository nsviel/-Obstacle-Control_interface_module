#! /usr/bin/python
#---------------------------------------------

from param import param_co

from scheme import scheme_link
from scheme import scheme_node
from scheme import scheme_color

import dearpygui.dearpygui as dpg


def build_scheme():
    create_scheme()
    init_scheme()

def create_scheme():
    # Construct node editor
    with dpg.node_editor(height = param_co.gui_scheme_height):
        scheme_node.node_controlium()
        scheme_node.node_pywardium()
        scheme_node.node_hubium()
        scheme_node.node_train()
        scheme_node.node_edge()
        scheme_node.node_edge_local()
        scheme_node.node_sncf()
        scheme_node.node_valeo()
        scheme_link.create_link()

def init_scheme():
    layer_control = scheme_color.color_layer_control()
    layer_train = scheme_color.color_layer_train()
    layer_edge = scheme_color.color_layer_edge()
    layer_cloud = scheme_color.color_layer_cloud()

    dpg.bind_item_theme("node_co", layer_control)
    dpg.bind_item_theme("node_py", layer_train)
    dpg.bind_item_theme("node_train", layer_train)
    dpg.bind_item_theme("node_hu", layer_edge)
    dpg.bind_item_theme("node_local", layer_edge)
    dpg.bind_item_theme("node_ed", layer_cloud)
    dpg.bind_item_theme("node_sncf", layer_cloud)
    dpg.bind_item_theme("node_valeo", layer_cloud)

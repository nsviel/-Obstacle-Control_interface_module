#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_color
from src.scheme.link import scheme_link_node
from src.scheme.link import scheme_link_color

import dearpygui.dearpygui as dpg


def create_link():
    scheme_link_node.create_link_train()
    scheme_link_node.create_link_edge_1()
    scheme_link_node.create_link_edge_2()

def update_link_color():
    scheme_link_color.update_color_train()
    scheme_link_color.update_color_edge_1()

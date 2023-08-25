#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_color
from src.scheme.link import link_node
from src.scheme.link import link_color

import dearpygui.dearpygui as dpg


def create_link():
    link_node.create_link_train()
    link_node.create_link_edge_1()
    link_node.create_link_edge_2()

def update_link_color():
    link_color.update_color_train()
    link_color.update_color_edge_1()
    link_color.update_color_edge_2()

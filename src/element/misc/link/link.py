#---------------------------------------------
from src.param import param_control
from src.gui.style import gui_color
from src.element.misc.link import link_node
from src.element.misc.link import link_color
from src.element.misc.link import link_ID
import dearpygui.dearpygui as dpg


class Link():
    def __init__(self):
        self.ID = link_ID.Link_ID()

    def build_links():
        link_node.build_link_ground()
        link_node.create_link_edge_1()
        link_node.create_link_edge_2()

    def update_links():
        link_color.update_color_train()
        link_color.update_color_edge_1()
        link_color.update_color_edge_2()

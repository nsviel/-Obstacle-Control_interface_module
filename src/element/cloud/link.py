#---------------------------------------------
from src.param import param_control
from src.utils import function
from src.gui.style import colorization
import dearpygui.dearpygui as dpg


class Link:
    def __init__(self, cloud):
        self.cloud = cloud
        self.link_control_ssd = function.id_generator();
        self.link_http_control_edge = function.id_generator();
        self.link_sock_l1_control_edge = function.id_generator();
        self.link_sock_l2_control_edge = function.id_generator();

    def setup(self, edge):
        dpg.add_node_link(self.cloud.ssd.ID.ID_node_input, self.cloud.control.ID.ID_ssd_connection, tag=self.link_control_ssd)
        dpg.add_node_link(self.cloud.control.ID.ID_http_client, edge.hub.ID.ID_http_server, tag=self.link_http_control_edge)
        dpg.add_node_link(edge.hub.ID.ID_sock_client_l1, self.cloud.control.ID.ID_sock_server_l1, tag=self.link_sock_l1_control_edge)
        dpg.add_node_link(edge.hub.ID.ID_sock_client_l2, self.cloud.control.ID.ID_sock_server_l2, tag=self.link_sock_l2_control_edge)

    def update(self):
        colorization.colorize_link_http(param_control.state_control["ssd"]["connected"], self.link_control_ssd)
        colorization.colorize_link_http(param_control.state_edge["hub"]["http"]["connected"], self.link_http_control_edge)
        colorization.colorize_link_socket(param_control.state_edge["hub"]["socket"]["l1_connected"], self.link_sock_l1_control_edge)
        colorization.colorize_link_socket(param_control.state_edge["hub"]["socket"]["l2_connected"], self.link_sock_l2_control_edge)

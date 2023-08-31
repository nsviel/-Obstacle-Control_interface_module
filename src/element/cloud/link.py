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
        self.update_dependencies()
        colorization.colorize_link_http(self.link_control_ssd, param_control.state_control["interface"]["ssd_connected"])
        colorization.colorize_link_http(self.link_http_control_edge, param_control.state_control["interface"]["edge"]["http_connected"])
        colorization.colorize_link_socket(self.link_sock_l1_control_edge, param_control.state_control["interface"]["edge"]["sock_l1_connected"])
        colorization.colorize_link_socket(self.link_sock_l2_control_edge, param_control.state_control["interface"]["edge"]["sock_l2_connected"])

    def update_dependencies(self):
        param_control.state_control["ssd"]["info"]["status"] = "Offline"
        if(param_control.state_control["interface"]["ssd_connected"]):
            param_control.state_control["ssd"]["info"]["status"] = "Online"

        if(param_control.state_control["interface"]["edge"]["http_connected"]):
            if(param_control.state_edge["interface"]["operator"]["broker_connected"]):
                param_control.state_cloud["operator"]["info"]["status"] = "Online"
        else:
            param_control.state_edge["interface"]["operator"]["broker_connected"] = False

#---------------------------------------------
from src.utils import function
from src.gui.style import colorization
from src.param import param_control
import dearpygui.dearpygui as dpg


class Link:
    def __init__(self, edge):
        self.edge = edge
        self.link_sock_hub_slam = function.id_generator();
        self.link_http_hub_slam = function.id_generator();
        self.link_http_hub_ai = function.id_generator();
        self.link_sock_l1_cap_hub = function.id_generator();
        self.link_sock_l2_cap_hub = function.id_generator();
        self.link_http_cap_hub = function.id_generator();
        self.link_http_hub_control = function.id_generator();
        self.link_mqtt_hub_operator = function.id_generator();

    def setup(self, ground, cloud):
        self.setup_internal()
        self.setup_external(ground, cloud)

    def setup_internal(self):
        dpg.add_node_link(self.edge.hub.ID.ID_sock_client_l1, self.edge.slam.ID.ID_sock_server, tag=self.link_sock_hub_slam)
        dpg.add_node_link(self.edge.hub.ID.ID_http_client, self.edge.slam.ID.ID_http_server, tag=self.link_http_hub_slam)
        dpg.add_node_link(self.edge.hub.ID.ID_http_client, self.edge.ai.ID.ID_http_server, tag=self.link_http_hub_ai)

    def setup_external(self, ground, cloud):
        dpg.add_node_link(ground.capture.ID.ID_sock_client_l1, self.edge.hub.ID.ID_sock_server_l1, tag=self.link_sock_l1_cap_hub)
        dpg.add_node_link(ground.capture.ID.ID_sock_client_l2, self.edge.hub.ID.ID_sock_server_l2, tag=self.link_sock_l2_cap_hub)
        dpg.add_node_link(ground.capture.ID.ID_http_server, self.edge.hub.ID.ID_http_server, tag=self.link_http_cap_hub)
        dpg.add_node_link(self.edge.hub.ID.ID_mqtt_client, cloud.operator.ID.ID_mqtt_broker, tag=self.link_mqtt_hub_operator)

    def update(self):
        colorization.colorize_link_socket(self.edge.state.state_component["slam"]["sock"]["connected"], self.link_sock_hub_slam)
        colorization.colorize_link_http(self.edge.state.state_component["slam"]["http"]["connected"], self.link_http_hub_slam)
        colorization.colorize_link_http(self.edge.state.state_component["ai"]["http"]["connected"], self.link_http_hub_ai)
        colorization.colorize_link_socket(self.edge.state.state_interface["train"]["sock"]["l1_connected"], self.link_sock_l1_cap_hub)
        colorization.colorize_link_socket(self.edge.state.state_interface["train"]["sock"]["l2_connected"], self.link_sock_l2_cap_hub)
        colorization.colorize_link_http(self.edge.state.state_interface["train"]["http"]["connected"], self.link_http_cap_hub)
        colorization.colorize_link_http(self.edge.state.state_interface["operator"]["mqtt"]["connected"], self.link_mqtt_hub_operator)

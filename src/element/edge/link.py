#---------------------------------------------
from src.param import param_control
from src.utils import function
from src.gui.style import colorization
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
        self.update_dependencies()
        colorization.colorize_link_http(self.link_http_hub_slam, param_control.state_edge["slam"]["http"]["connected"])
        colorization.colorize_link_http(self.link_http_hub_ai, param_control.state_edge["ai"]["http"]["connected"])
        colorization.colorize_link_http(self.link_http_cap_hub, param_control.state_edge["interface"]["capture"]["http_connected"])
        colorization.colorize_link_http(self.link_mqtt_hub_operator, param_control.state_edge["interface"]["operator"]["broker_connected"])

        colorization.colorize_link_socket(self.link_sock_hub_slam, param_control.state_edge["slam"]["socket"]["connected"])
        colorization.colorize_link_socket(self.link_sock_l1_cap_hub, param_control.state_edge["interface"]["capture"]["sock_l1_connected"])
        colorization.colorize_link_socket(self.link_sock_l2_cap_hub, param_control.state_edge["interface"]["capture"]["sock_l2_connected"])

    def update_dependencies(self):
        if(param_control.state_control["interface"]["edge"]["http_connected"]):
            param_control.state_edge["hub"]["info"]["status"] = "Online"
            if(param_control.state_edge["ai"]["http"]["connected"]):
                param_control.state_edge["ai"]["info"]["status"] = "Online"
            else:
                param_control.state_edge["ai"]["info"]["status"] = "Offline"
            if(param_control.state_edge["slam"]["http"]["connected"]):
                param_control.state_edge["slam"]["info"]["status"] = "Online"
            else:
                param_control.state_edge["slam"]["info"]["status"] = "Offline"
                param_control.state_edge["slam"]["socket"]["connected"] = False
        else:
            param_control.state_edge["hub"]["info"]["status"] = "Offline"
            param_control.state_edge["data"]["nb_frame"] = 0
            param_control.state_edge["data"]["nb_prediction"] = 0
            param_control.state_edge["hub"]["info"]["nb_thread"] = 0
            param_control.state_edge["ai"]["http"]["connected"] = False
            param_control.state_edge["slam"]["socket"]["connected"] = False
            param_control.state_edge["slam"]["http"]["connected"] = False

        if(param_control.state_edge["slam"]["info"]["status"] == "Offline"):
            param_control.state_edge["slam"]["socket"]["connected"] = False

        if(param_control.state_network["mongodb"]["connected"]):
            param_control.state_network["mongodb"]["status"] = "Online"
        else:
            param_control.state_network["mongodb"]["status"] = "Offline"

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
        colorization.colorize_link_http(param_control.state_edge["slam"]["http_connected"], self.link_http_hub_slam)
        colorization.colorize_link_http(param_control.state_edge["ai"]["http_connected"], self.link_http_hub_ai)
        colorization.colorize_link_http(param_control.state_ground["capture"]["http_connected"], self.link_http_cap_hub)
        colorization.colorize_link_http(param_control.state_cloud["operator"]["broker_connected"], self.link_mqtt_hub_operator)

        colorization.colorize_link_socket(param_control.state_edge["slam"]["sock_connected"], self.link_sock_hub_slam)
        #colorization.colorize_link_socket(self.edge.state.state_interface["train"]["sock"]["l1_connected"], self.link_sock_l1_cap_hub)
        #colorization.colorize_link_socket(self.edge.state.state_interface["train"]["sock"]["l2_connected"], self.link_sock_l2_cap_hub)

    def update_dependencies():

        param_control.state_ground["capture"]["info"]["status"] = "Offline"
        param_control.state_edge["hub"]["info"]["status"] = "Offline"
        param_control.state_edge["slam"]["info"]["status"] = "Offline"
        param_control.state_edge["ai"]["info"]["status"] = "Offline"
        param_control.state_cloud["operator"]["info"]["status"] = "Offline"
        param_control.state_network["mongodb"]["info"]["status"] = "Offline"

        param_control.status_control = "Online"
        if(param_control.state_control["ssd"]["connected"]):
            param_control.status_ssd = "Online"

        if(param_control.state_edge["hub"]["http"]["connected"]):
            param_control.status_edge = "Online"
            if(param_control.state_ground["capture"]["http_connected"]):
                param_control.status_capture = "Online"
                if(param_control.state_ground["lidar_1"]["connected"]):
                    param_control.status_lidar_1 = "Online"
                if(param_control.state_ground["lidar_2"]["connected"]):
                    param_control.status_lidar_2 = "Online"
            if(param_control.state_edge["ai"]["http_connected"]):
                param_control.status_ai = "Online"
            if(param_control.state_edge["slam"]["http_connected"]):
                param_control.status_slam = "Online"
            if(param_control.state_cloud["operator"]["broker_connected"]):
                param_control.status_operator = "Online"

        if(param_control.status_edge == "Offline"):
            param_control.state_edge["data"]["nb_frame"] = 0
            param_control.state_edge["data"]["nb_prediction"] = 0
            param_control.state_edge["hub"]["nb_thread"] = 0
            param_control.state_cloud["operator"]["broker_connected"] = False
            param_control.state_edge["ai"]["http_connected"] = False
            param_control.state_edge["slam"]["sock_connected"] = False
            param_control.state_edge["slam"]["http_connected"] = False
            param_control.state_ground["capture"]["http_connected"] = False
            param_control.state_ground["capture"]["sock_l1_connected"] = False
            param_control.state_ground["capture"]["sock_l2_connected"] = False

        if(param_control.status_capture == "Offline"):
            param_control.state_ground["capture"]["nb_thread"] = 0
            param_control.state_ground["nb_thread"] = 0

            param_control.state_ground["lidar_1"]["connected"] = False
            param_control.state_ground["lidar_1"]["activated"] = False
            param_control.state_ground["lidar_1"]["running"] = False
            param_control.state_ground["lidar_1"]["packet"]["value"] = 0
            param_control.state_ground["lidar_1"]["packet"]["min"] = 0
            param_control.state_ground["lidar_1"]["packet"]["mean"] = 0
            param_control.state_ground["lidar_1"]["packet"]["max"] = 0
            param_control.state_ground["lidar_1"]["throughput"]["value"] = 0
            param_control.state_ground["lidar_1"]["throughput"]["min"] = 0
            param_control.state_ground["lidar_1"]["throughput"]["mean"] = 0
            param_control.state_ground["lidar_1"]["throughput"]["max"] = 0

            param_control.state_ground["lidar_2"]["connected"] = False
            param_control.state_ground["lidar_2"]["activated"] = False
            param_control.state_ground["lidar_2"]["running"] = False
            param_control.state_ground["lidar_2"]["packet"]["min"] = 0
            param_control.state_ground["lidar_2"]["packet"]["mean"] = 0
            param_control.state_ground["lidar_2"]["packet"]["max"] = 0
            param_control.state_ground["lidar_2"]["throughput"]["value"] = 0
            param_control.state_ground["lidar_2"]["throughput"]["min"] = 0
            param_control.state_ground["lidar_2"]["throughput"]["mean"] = 0
            param_control.state_ground["lidar_2"]["throughput"]["max"] = 0

        if(param_control.status_slam == "Offline"):
            param_control.state_edge["slam"]["sock_connected"] = False

        if(param_control.state_network["mongodb"]["connected"]):
            param_control.status_db = "Online"

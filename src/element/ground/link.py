#---------------------------------------------
from src.utils import function
from src.gui.style import colorization
from src.param import param_control
import dearpygui.dearpygui as dpg


class Link:
    def __init__(self, ground):
        self.ground = ground
        self.link_l1_capture = function.id_generator();
        self.link_l2_capture = function.id_generator();

    def setup(self):
        dpg.add_node_link(self.ground.lidar_1.ID.ID_sock_client, self.ground.capture.ID.ID_sock_server_l1, tag=self.link_l1_capture)
        dpg.add_node_link(self.ground.lidar_2.ID.ID_sock_client, self.ground.capture.ID.ID_sock_server_l2, tag=self.link_l2_capture)

    def update(self):
        self.update_dependencies()
        colorization.colorize_link_socket(self.link_l1_capture, param_control.state_ground["lidar_1"]["info"]["connected"])
        colorization.colorize_link_socket(self.link_l2_capture, param_control.state_ground["lidar_2"]["info"]["connected"])

    def update_dependencies(self):
        param_control.state_ground["capture"]["info"]["status"] = "Offline"
        param_control.state_ground["lidar_1"]["info"]["status"] = "Offline"
        param_control.state_ground["lidar_2"]["info"]["status"] = "Offline"

        if(param_control.state_control["interface"]["edge"]["http_connected"]):
            if(param_control.state_edge["interface"]["capture"]["http_connected"]):
                param_control.state_ground["capture"]["info"]["status"] = "Online"
                if(param_control.state_ground["lidar_1"]["info"]["connected"]):
                    param_control.state_ground["lidar_1"]["info"]["status"] = "Online"
                if(param_control.state_ground["lidar_2"]["info"]["connected"]):
                    param_control.state_ground["lidar_2"]["info"]["status"] = "Online"
        else:
            param_control.state_edge["interface"]["capture"]["http_connected"] = False
            param_control.state_ground["capture"]["socket"]["l1_connected"] = False
            param_control.state_ground["capture"]["socket"]["l2_connected"] = False

        if(param_control.state_ground["capture"]["info"]["status"] == "Offline"):
            param_control.state_ground["capture"]["info"]["nb_thread"] = 0

            param_control.state_ground["lidar_1"]["info"]["connected"] = False
            param_control.state_ground["lidar_1"]["info"]["activated"] = False
            param_control.state_ground["lidar_1"]["motor"]["running"] = False
            param_control.state_ground["lidar_1"]["packet"]["value"] = 0
            param_control.state_ground["lidar_1"]["packet"]["min"] = 0
            param_control.state_ground["lidar_1"]["packet"]["mean"] = 0
            param_control.state_ground["lidar_1"]["packet"]["max"] = 0
            param_control.state_ground["lidar_1"]["throughput"]["value"] = 0
            param_control.state_ground["lidar_1"]["throughput"]["min"] = 0
            param_control.state_ground["lidar_1"]["throughput"]["mean"] = 0
            param_control.state_ground["lidar_1"]["throughput"]["max"] = 0

            param_control.state_ground["lidar_2"]["info"]["connected"] = False
            param_control.state_ground["lidar_2"]["info"]["activated"] = False
            param_control.state_ground["lidar_2"]["motor"]["running"] = False
            param_control.state_ground["lidar_2"]["packet"]["min"] = 0
            param_control.state_ground["lidar_2"]["packet"]["mean"] = 0
            param_control.state_ground["lidar_2"]["packet"]["max"] = 0
            param_control.state_ground["lidar_2"]["throughput"]["value"] = 0
            param_control.state_ground["lidar_2"]["throughput"]["min"] = 0
            param_control.state_ground["lidar_2"]["throughput"]["mean"] = 0
            param_control.state_ground["lidar_2"]["throughput"]["max"] = 0

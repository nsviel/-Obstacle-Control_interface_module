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
        colorization.colorize_link_socket(self.ground.state["component"]["lidar_1"]["connected"], self.link_l1_capture)
        colorization.colorize_link_socket(self.ground.state["component"]["lidar_2"]["connected"], self.link_l2_capture)

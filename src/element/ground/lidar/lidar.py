#---------------------------------------------
from src.element.ground.lidar import lidar_ID
from src.element.ground.lidar import lidar_node
from src.element.ground.lidar import lidar_window
from src.gui.background import gui_handler


# Generic LiDAR class
class Lidar:
    def __init__(self, ID):
        self.ID = lidar_ID.Lidar_ID(ID)
        self.node = lidar_node.Lidar_node(self.ID)
        self.window = lidar_window.Lidar_window(self.ID)

    def setup_handler(self):
        gui_handler.add_node_handler(self.ID, self.window)

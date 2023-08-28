#---------------------------------------------
from src.element.ground.capture import capture
from src.element.ground.lidar import lidar
from src.element.ground import link
from src.utils import parser_json


class Ground:
    def __init__(self, ID):
        self.ID_ground = "ground_" + str(ID)
        self.capture = capture.Capture()
        self.lidar_1 = lidar.Lidar(1)
        self.lidar_2 = lidar.Lidar(2)
        self.link = link.Link(self)

    # Node
    def build_nodes(self):
        self.capture.node.build()
        self.lidar_1.node.build()
        self.lidar_2.node.build()
    def update_nodes(self):
        self.capture.node.update()
        self.lidar_1.node.update()
        self.lidar_2.node.update()

    # Window
    def build_windows(self):
        self.capture.window.build()
        self.lidar_1.window.build()
        self.lidar_2.window.build()
    def update_windows(self):
        self.capture.window.update()
        self.lidar_1.window.update()
        self.lidar_2.window.update()

    # Event
    def setup_handlers(self):
        self.capture.setup_handler()
        self.lidar_1.setup_handler()
        self.lidar_2.setup_handler()
    def set_invisible_all(self):
        self.capture.window.set_invisible()
        self.lidar_1.window.set_invisible()
        self.lidar_2.window.set_invisible()

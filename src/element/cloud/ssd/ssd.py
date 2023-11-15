#---------------------------------------------
from src.element.cloud.ssd import ssd_ID
from src.element.cloud.ssd import ssd_node
from src.element.cloud.ssd import ssd_window
from src.gui.background import gui_handler


# Generic LiDAR class
class Ssd:
    def __init__(self):
        self.ID = ssd_ID.Ssd_ID()
        self.node = ssd_node.Ssd_node(self.ID)
        self.window = ssd_window.Ssd_window(self.ID)

    def setup_handler(self):
        gui_handler.add_node_handler(self.ID, self.window)

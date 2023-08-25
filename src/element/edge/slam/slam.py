#---------------------------------------------
from src.element.edge.slam import slam_ID
from src.element.edge.slam import slam_node
from src.element.edge.slam import slam_window
from src.gui.background import gui_handler


class Slam:
    def __init__(self, ID):
        self.ID = slam_ID.Slam_ID(ID)
        self.node = slam_node.Slam_node(self.ID)
        self.window = slam_window.Slam_window(self.ID)

    def setup_handler(self):
        gui_handler.add_node_handler(self.ID, self.window)

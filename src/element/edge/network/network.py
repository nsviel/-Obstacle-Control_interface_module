#---------------------------------------------
from src.element.edge.network import network_ID
from src.element.edge.network import network_node
from src.element.edge.network import network_window
from src.gui.background import gui_handler


class Network:
    def __init__(self, ID):
        self.ID = network_ID.Network_ID(ID)
        self.node = network_node.Network_node(self.ID)
        self.window = network_window.Network_window(self.ID)

    def setup_handler(self):
        gui_handler.add_node_handler(self.ID, self.window)

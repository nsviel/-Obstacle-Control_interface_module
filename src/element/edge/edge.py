#---------------------------------------------
from src.element.edge.hub import hub
from src.element.edge.slam import slam
from src.element.edge.data import data
from src.element.edge.ai import ai
from src.element.edge.network import network
from src.element.edge import link
from src.utils import parser_json


class Edge:
    def __init__(self, ID):
        self.ID_edge = "edge_" + str(ID)
        self.hub = hub.Hub(self.ID_edge)
        self.slam = slam.Slam(self.ID_edge)
        self.data = data.Data(self.ID_edge)
        self.ai = ai.Ai(self.ID_edge)
        self.network = network.Network(self.ID_edge)
        self.link = link.Link(self)

    # Node
    def build_nodes(self):
        self.slam.node.build()
        self.ai.node.build()
        self.data.node.build()
        self.hub.node.build()
        self.network.node.build()
    def update_nodes(self):
        self.slam.node.update()
        self.ai.node.update()
        self.data.node.update()
        self.hub.node.update()
        self.network.node.update()

    # Window
    def build_windows(self):
        self.slam.window.build()
        self.ai.window.build()
        self.data.window.build()
        self.hub.window.build()
        self.network.window.build()
    def update_windows(self):
        self.slam.window.update()
        self.ai.window.update()
        self.data.window.update()
        self.hub.window.update()
        self.network.window.update()

    # Event
    def setup_handlers(self):
        self.slam.setup_handler()
        self.ai.setup_handler()
        self.data.setup_handler()
        self.hub.setup_handler()
        self.network.setup_handler()
    def set_invisible_all(self):
        self.slam.window.set_invisible()
        self.ai.window.set_invisible()
        self.data.window.set_invisible()
        self.hub.window.set_invisible()
        self.network.window.set_invisible()

#---------------------------------------------
from src.element.edge.hub import hub_ID
from src.element.edge.hub import hub_node
from src.element.edge.hub import hub_window
from src.gui.background import gui_handler


class Hub:
    def __init__(self, ID):
        self.ID = hub_ID.Hub_ID(ID)
        self.node = hub_node.Hub_node(self.ID)
        self.window = hub_window.Hub_window(self.ID)

    def setup_handler(self):
        gui_handler.add_node_handler(self.ID, self.window)

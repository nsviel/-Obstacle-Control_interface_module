#---------------------------------------------
from src.element.edge.ai import ai_ID
from src.element.edge.ai import ai_node
from src.element.edge.ai import ai_window
from src.gui.background import gui_handler


class Ai:
    def __init__(self, ID_edge):
        self.ID = ai_ID.Ai_ID(ID_edge)
        self.node = ai_node.Ai_node(self.ID)
        self.window = ai_window.Ai_window(self.ID)

    def setup_handler(self):
        gui_handler.add_node_handler(self.ID, self.window)

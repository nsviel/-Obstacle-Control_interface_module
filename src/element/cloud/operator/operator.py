#---------------------------------------------
from src.element.cloud.operator import operator_ID
from src.element.cloud.operator import operator_node
from src.element.cloud.operator import operator_window
from src.gui.background import gui_handler


class Operator:
    def __init__(self):
        self.ID = operator_ID.Operator_ID()
        self.node = operator_node.Operator_node(self.ID)
        self.window = operator_window.Operator_window(self.ID)

    def setup_handler(self):
        gui_handler.add_node_handler(self.ID, self.window)

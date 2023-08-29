#---------------------------------------------
from src.element.cloud.control import control_ID
from src.element.cloud.control import control_node
from src.element.cloud.control import control_window
from src.gui.background import gui_handler


class Control:
    def __init__(self):
        self.ID = control_ID.Control_ID()
        self.node = control_node.Control_node(self.ID)
        self.window = control_window.Control_window(self.ID)

    def setup_handler(self):
        gui_handler.add_node_handler(self.ID, self.window)

#---------------------------------------------
from src.element.ground.capture import capture_ID
from src.element.ground.capture import capture_node
from src.element.ground.capture import capture_window
from src.gui.background import gui_handler


class Capture:
    def __init__(self):
        self.ID = capture_ID.Capture_ID()
        self.node = capture_node.Capture_node(self.ID)
        self.window = capture_window.Capture_window(self.ID)

    def setup_handler(self):
        gui_handler.add_node_handler(self.ID, self.window)

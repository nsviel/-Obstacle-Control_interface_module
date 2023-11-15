#---------------------------------------------
from src.element.edge.data import data_ID
from src.element.edge.data import data_node
from src.element.edge.data import data_window
from src.element.edge.data import data_plot
from src.gui.background import gui_handler


class Data:
    def __init__(self, ID):
        self.ID = data_ID.Data_ID(ID)
        self.plot = data_plot.Data_plot(self.ID)
        self.node = data_node.Data_node(self.ID, self.plot)
        self.window = data_window.Data_window(self.ID)

    def setup_handler(self):
        gui_handler.add_node_handler(self.ID, self.window)

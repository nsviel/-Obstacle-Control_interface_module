#---------------------------------------------
from src.element.cloud.control import control
from src.element.cloud.operator import operator
from src.element.cloud.ssd import ssd
from src.element.cloud import link
from src.element.cloud import state
from src.utils import parser_json


class Cloud:
    def __init__(self, ID):
        self.ID_cloud = "cloud_" + str(ID)
        self.control = control.Control()
        self.operator = operator.Operator()
        self.ssd = ssd.Ssd()
        self.link = link.Link(self)
        self.state = state.State()

    def build_nodes(self):
        self.control.node.build()
        self.operator.node.build()
        self.ssd.node.build()

    def build_windows(self):
        self.control.window.build()
        self.operator.window.build()
        self.ssd.window.build()

    def setup_handlers(self):
        self.control.setup_handler()
        self.operator.setup_handler()
        self.ssd.setup_handler()

#---------------------------------------------
from src.utils import function
from src.gui.background import texture


class Link_ID:
    def __init__(self):
        self.init_ID_ground()

    def init_ID_ground(self):
        self.ID_l1_capture = function.id_generator();
        self.ID_l2_capture = function.id_generator();
        self.ID_l1_capture_edge_1 = function.id_generator();
        self.ID_l2_capture_edge_1 = function.id_generator();
        self.ID_http_capture_edge_1 = function.id_generator();

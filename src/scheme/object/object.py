#---------------------------------------------
from src.scheme.object import obj_control
from src.scheme.object import obj_edge
from src.scheme.object import obj_operator
from src.scheme.object import obj_ssd
from src.scheme.object import obj_capture
from src.scheme.object import obj_train


class Object():
    def init_object(self):
        self.ssd = obj_ssd.SSD()
        self.control = obj_control.Control()
        self.operator = obj_operator.Operator()
        self.train = obj_train.Train()
        self.capture = obj_capture.Capture()
        self.edge_1 = obj_edge.Edge()
        self.edge_2 = obj_edge.Edge()

    ssd = []
    control = []
    operator = []
    train = []
    capture = []
    edge_1 = []
    edge_2 = []

object = Object()

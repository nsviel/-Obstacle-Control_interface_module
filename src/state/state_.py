from src.utils import parser_json


class State_edge_1:
    def __init__(self):
        self.component = parser_json.load_state("src/state/edge_1/state_component.json")
        self.interface = parser_json.load_state("src/state/edge_1/state_interface.json")
        self.kpi = parser_json.load_state("src/state/edge_1/state_kpi.json")

class State_edge_2:
    def __init__(self):
        self.component = parser_json.load_state("src/state/edge_2/state_component.json")
        self.interface = parser_json.load_state("src/state/edge_2/state_interface.json")
        self.kpi = parser_json.load_state("src/state/edge_2/state_kpi.json")

class State_cloud:
    def __init__(self):
        self.component = parser_json.load_state("src/state/cloud/state_component.json")
        self.interface = parser_json.load_state("src/state/cloud/state_interface.json")

class State_ground:
    def __init__(self):
        self.capture = parser_json.load_state("src/state/ground/state_capture.json")
        self.lidar_1 = parser_json.load_state("src/state/ground/state_lidar_1.json")
        self.lidar_2 = parser_json.load_state("src/state/ground/state_lidar_2.json")
        self.interface = parser_json.load_state("src/state/ground/state_interface.json")

class State:
    def __init__(self):
        self.edge_1 = State_edge_1()
        self.edge_2 = State_edge_2()
        self.cloud = State_cloud()
        self.ground = State_ground()

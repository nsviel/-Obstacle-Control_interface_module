from src.utils import parser_json


class State:
    def __init__(self, ID):
        self.init_state_edge_1()
        self.init_state_edge_2()

    def init_state_edge_1(self):
        ID = "edge_1"
        self.edge_1.state_component = parser_json.load_state("src/state/"+ str(ID) +"/state_component.json")
        self.edge_1.state_interface = parser_json.load_state("src/state/"+ str(ID) +"/state_interface.json")
        self.edge_1.state_kpi = parser_json.load_state("src/state/"+ str(ID) +"/state_kpi.json")
        self.edge_1.state_component["ID"] = ID

    def init_state_edge_2(self):
        ID = "edge_2"
        self.edge_2.state_component = parser_json.load_state("src/state/"+ str(ID) +"/state_component.json")
        self.edge_2.state_interface = parser_json.load_state("src/state/"+ str(ID) +"/state_interface.json")
        self.edge_2.state_kpi = parser_json.load_state("src/state/"+ str(ID) +"/state_kpi.json")
        self.edge_2.state_component["ID"] = ID

state = State()

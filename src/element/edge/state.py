from src.utils import parser_json


class State:
    def __init__(self, ID):
        self.state_component = parser_json.load_state("src/state/"+ str(ID) +"/state_component.json")
        self.state_interface = parser_json.load_state("src/state/"+ str(ID) +"/state_interface.json")
        self.state_kpi = parser_json.load_state("src/state/"+ str(ID) +"/state_kpi.json")

        self.state_component["ID"] = ID

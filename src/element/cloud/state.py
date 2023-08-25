from src.utils import parser_json


class State:
    def __init__(self):
        self.state_component = parser_json.load_state("src/state/cloud/state_component.json")
        self.state_interface = parser_json.load_state("src/state/cloud/state_interface.json")

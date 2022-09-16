#---------------------------------------------
from param import param_co

import json


def load_data_from_file(path):
    file = open(path, "r")
    data = json.load(file)
    return data

def load_data_from_file_b(path):
    f = open(path)
    data = json.dumps(json.load(f))
    return data

def load_data_from_file_utf8(path):
    file = open(path)
    data = json.load(file)
    data_encoded = json.dumps(data).encode(encoding='utf_8')
    return data_encoded

def upload_file(path, data):
    file = open(path, "w")
    json.dump(data, file, indent=4)

def upload_state():
    file = open(param_co.path_state_co, "w")
    json.dump(param_co.state_co, file, indent=4)

def update_state_file(path, data):
    if(len(data) != 0):
        file = open(path, 'w')
        data_loaded = json.loads(data)
        json.dump(data_loaded, file, indent=4)

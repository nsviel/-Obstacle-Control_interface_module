#---------------------------------------------
from src.param import param_control
import dearpygui.dearpygui as dpg
import json
import os


def load_state(path):
    try:
        file = open(path, "r")
        data = json.load(file)
        return data
    except:
        print("[error] path %s does not exists"% path)
        dir = os.path.dirname(os.path.abspath(path))
        name = os.path.basename(path)
        generic = dir + "/../generic/" + name
        file = open(generic, "r")
        data = json.load(file)
        return data

def load_pos_from_json(name):
    file = open(param_control.path_node_coordinate, "r")
    data = json.load(file)
    try:
        coord = data[name]
    except:
        coord = [0, 0]
        print("[error] name %s does not exists"% name)
    return coord

def get_pos_from_json():
    file = open(param_control.path_node_coordinate, "r")
    data = json.load(file)
    return data

def load_data_from_file(path):
    file = open(path, "r")
    data = json.load(file)
    return data

def load_data_from_file_b(path):
    f = open(path)
    data = json.dumps(json.load(f))
    return data

def load_state_utf8(path):
    try:
        file = open(path)
        data = json.load(file)
        data_encoded = json.dumps(data).encode(encoding='utf_8')
        return data_encoded
    except:
        pass

def upload_file(path, data):
    file = open(path, "w")
    json.dump(data, file, indent=4)

def upload_state():
    file = open(param_control.path_state_control, "w")
    json.dump(param_control.state_control, file, indent=4)

def update_state_file(path, data):
    if(len(data) != 0):
        file = open(path, 'w')
        data_loaded = json.loads(data)
        json.dump(data_loaded, file, indent=4)

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

def load_pos_from_json(name):
    file = open(param_control.path_node_pose, "r")
    data = json.load(file)
    try:
        coord = data[name]
    except:
        coord = [0, 0]
        print("[error] name %s does not exists"% name)
    return coord

def get_pos_from_json():
    file = open(param_control.path_node_pose, "r")
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

def upload_file(path, data):
    file = open(path, "w")
    json.dump(data, file, indent=4)

def update_state_file(path, data):
    if(len(data) != 0):
        file = open(path, 'w')
        data_loaded = json.loads(data)
        json.dump(data_loaded, file, indent=4)

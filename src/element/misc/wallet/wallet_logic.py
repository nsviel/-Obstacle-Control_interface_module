#---------------------------------------------
from src.param import param_control
from src.utils import parser_json
import pandas as pd
import json


# Initialisation function
def initialization():
    read_wallet_file()
    determine_adresse()
def determine_adresse():
    param_control.state_edge["hub"]["info"]["add"] = get_add_from_ip(param_control.state_edge["hub"]["info"]["ip"])
    param_control.state_cloud["operator"]["info"]["add"] = get_add_from_ip(param_control.state_cloud["operator"]["info"]["ip"])
    param_control.state_ground["capture"]["info"]["add"] = get_add_from_ip(param_control.state_ground["capture"]["info"]["ip"])
    param_control.state_ground["lidar_1"]["info"]["add"] = get_add_from_ip(param_control.state_ground["lidar_1"]["info"]["ip"])
    param_control.state_ground["lidar_2"]["info"]["add"] = get_add_from_ip(param_control.state_ground["lidar_2"]["info"]["ip"])

# IO
def read_wallet_file():
    param_control.wallet = parser_json.load_data_from_file(param_control.wallet_path)
def write_wallet_file():
    parser_json.upload_file(param_control.wallet_path, param_control.wallet)

# Add / Suppress wallet element
def add_new_item(new_add, new_ip):
    new_item = {new_add:new_ip}
    param_control.wallet.update(new_item)
    write_wallet_file()
def remove_item(add):
    param_control.wallet.pop(add)
    write_wallet_file()
def remove_item_id(id):
    del param_control.wallet[int(id)]
    write_wallet_file()

# Subfunction
def get_ip_from_add(add):
    return param_control.wallet[add]
def get_add_from_ip(ip):
    for key, value in param_control.wallet.items():
        if(ip == value):
            return param_control.wallet[key]
    return "-"

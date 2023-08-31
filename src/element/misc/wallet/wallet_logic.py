#---------------------------------------------
from src.param import param_control
from src.utils import parser_json
import pandas as pd
import json


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
            return key
    return "-"

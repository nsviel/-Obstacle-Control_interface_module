#---------------------------------------------
from src.param import param_control
from src.utils import parser_json
import pandas as pd
import json


class Wallet_logic:
    def __init__(self):
        self.wallet = {}
        self.read_wallet_file()

    # IO
    def read_wallet_file(self):
        self.wallet = parser_json.load_data_from_file(param_control.path_wallet)
    def write_wallet_file(self):
        parser_json.upload_file(param_control.path_wallet, self.wallet)
    def get_list_add(self):
        return list(self.wallet.keys())

    # Add / Suppress wallet element
    def add_new_item(self, new_add, new_ip):
        new_item = {new_add:new_ip}
        self.wallet.update(new_item)
        self.write_wallet_file()
    def remove_item_id(self, id):
        self.wallet.pop(list(self.wallet.keys())[int(id)])
        self.write_wallet_file()

    # Subfunction
    def get_ip_from_add(self, add):
        return self.wallet[add]
    def get_add_from_ip(self, ip):
        for key, value in self.wallet.items():
            if(ip == value):
                return key
        return "-"

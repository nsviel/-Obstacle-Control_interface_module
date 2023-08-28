#---------------------------------------------
from src.param import param_control
from src.utils import parser_json

import pandas as pd


def initialization():
    read_wallet()
    determine_adresse()

def add_new_item(new_add, new_ip):
    if(new_add != "" and new_ip != ""):
        param_control.wallet_add.append(new_add)
        param_control.wallet_ip.append(new_ip)
        write_wallet()

def remoprocessing_item(item):
    for i in range(0, len(param_control.wallet_add)):
        if(param_control.wallet_add[i] == item):
            del param_control.wallet_add[i]
            del param_control.wallet_ip[i]
            write_wallet()
            break

def remoprocessing_item_id(id):
    del param_control.wallet_add[int(id)]
    del param_control.wallet_ip[int(id)]
    write_wallet()

def get_ip_from_key(key):
    for i in range(0, len(param_control.wallet_add)):
        if(param_control.wallet_add[i] == key):
            return param_control.wallet_ip[i]
    return "None"

def get_key_from_ip(ip):
    for i in range(0, len(param_control.wallet_add)):
        if(param_control.wallet_ip[i] == ip):
            return param_control.wallet_add[i]
    return "-"

def read_wallet():
    pass
def read_wallet_():
    X = pd.read_csv('src/element/wallet/wallet.txt', sep=" ", header=None)
    param_control.wallet_add = list()
    param_control.wallet_ip = list()
    for i in range(0, len(X[0])):
        param_control.wallet_add.append(str(X[0][i]))
        param_control.wallet_ip.append(str(X[1][i]))

def write_wallet():
    file = open("src/element/wallet/wallet.txt","w")
    #for i in range(0, len(param_control.wallet_add)):
        #file.write(param_control.wallet_add[i])
    #    file.write(" ")
        #file.write(param_control.wallet_ip[i])
    #    file.write("\n")

def determine_adresse():
    param_control.state_control["edge"]["add"] = get_key_from_ip(param_control.state_control["edge"]["ip"])
    param_control.state_edge["cloud_operator"]["add"] = get_key_from_ip(param_control.state_edge["cloud_operator"]["broker_ip"])
    param_control.state_edge["module_capture"]["add"] = get_key_from_ip(param_control.state_edge["module_capture"]["ip"])
    param_control.state_capture["lidar_1"]["add"] = get_key_from_ip(param_control.state_capture["lidar_1"]["ip"])
    param_control.state_capture["lidar_2"]["add"] = get_key_from_ip(param_control.state_capture["lidar_2"]["ip"])
    parser_json.upload_state()

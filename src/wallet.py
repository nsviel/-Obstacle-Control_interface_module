#---------------------------------------------
from param import param_co
from src import parser_json

import pandas as pd


def add_new_item(new_add, new_ip):
    if(new_add != "" and new_ip != ""):
        param_co.wallet_add.append(new_add)
        param_co.wallet_ip.append(new_ip)
        write_wallet()

def remove_item(item):
    for i in range(0, len(param_co.wallet_add)):
        if(param_co.wallet_add[i] == item):
            del param_co.wallet_add[i]
            del param_co.wallet_ip[i]
            write_wallet()
            break

def remove_item_id(id):
    del param_co.wallet_add[int(id)]
    del param_co.wallet_ip[int(id)]
    write_wallet()

def get_ip_from_key(key):
    for i in range(0, len(param_co.wallet_add)):
        if(param_co.wallet_add[i] == key):
            return param_co.wallet_ip[i]
    return "None"

def get_key_from_ip(ip):
    for i in range(0, len(param_co.wallet_add)):
        if(param_co.wallet_ip[i] == ip):
            return param_co.wallet_add[i]
    return "-"

def read_wallet():
    X = pd.read_csv('src/wallet.txt', sep=" ", header=None)
    param_co.wallet_add = list()
    param_co.wallet_ip = list()
    for i in range(0, len(X[0])):
        param_co.wallet_add.append(str(X[0][i]))
        param_co.wallet_ip.append(str(X[1][i]))

def write_wallet():
    file = open("src/wallet.txt","w")
    for i in range(0, len(param_co.wallet_add)):
        file.write(param_co.wallet_add[i])
        file.write(" ")
        file.write(param_co.wallet_ip[i])
        file.write("\n")

def determine_adresse():
    param_co.state_co["hubium"]["add"] = get_key_from_ip(param_co.state_co["hubium"]["ip"])
    param_co.state_hu["edge"]["add"] = get_key_from_ip(param_co.state_hu["edge"]["ip"])
    param_co.state_hu["sncf"]["add"] = get_key_from_ip(param_co.state_hu["sncf"]["broker_ip"])
    param_co.state_hu["pywardium"]["add"] = get_key_from_ip(param_co.state_hu["pywardium"]["ip"])
    param_co.state_py["lidar_1"]["add"] = get_key_from_ip(param_co.state_py["lidar_1"]["ip"])
    param_co.state_py["lidar_2"]["add"] = get_key_from_ip(param_co.state_py["lidar_2"]["ip"])
    parser_json.upload_state()

#---------------------------------------------
from src.param import param_control
from src.utils import parser_json
import pandas as pd


# Initialisation function
def initialization():
    read_wallet_file()
    determine_adresse()
def determine_adresse():
    param_control.state_edge["component"]["hub"]["info"]["add"] = get_key_from_ip(param_control.state_edge["component"]["hub"]["info"]["ip"])
    param_control.state_edge["interface"]["operator"]["add"] = get_key_from_ip(param_control.state_edge["interface"]["operator"]["broker_ip"])
    param_control.state_edge["interface"]["capture"]["add"] = get_key_from_ip(param_control.state_edge["interface"]["capture"]["ip"])
    param_control.state_ground["lidar_1"]["info"]["add"] = get_key_from_ip(param_control.state_ground["lidar_1"]["info"]["ip"])
    param_control.state_ground["lidar_2"]["info"]["add"] = get_key_from_ip(param_control.state_ground["lidar_2"]["info"]["ip"])
    parser_json.upload_state()

# IO
def read_wallet_file():
    X = pd.read_csv('src/element/misc/wallet/wallet.txt', sep=" ", header=None)
    param_control.wallet_add = list()
    param_control.wallet_ip = list()
    for i in range(0, len(X[0])):
        param_control.wallet_add.append(str(X[0][i]))
        param_control.wallet_ip.append(str(X[1][i]))
def write_wallet_file():
    file = open("src/element/misc/wallet/wallet.txt","w")
    for i in range(0, len(param_control.wallet_add)):
        file.write(param_control.wallet_add[i])
        file.write(" ")
        file.write(param_control.wallet_ip[i])
        file.write("\n")

# Add / Suppress wallet element
def add_new_item(new_add, new_ip):
    if(new_add != "" and new_ip != ""):
        param_control.wallet_add.append(new_add)
        param_control.wallet_ip.append(new_ip)
        write_wallet_file()
def remove_item(item):
    for i in range(0, len(param_control.wallet_add)):
        if(param_control.wallet_add[i] == item):
            del param_control.wallet_add[i]
            del param_control.wallet_ip[i]
            write_wallet_file()
            break
def remove_item_id(id):
    del param_control.wallet_add[int(id)]
    del param_control.wallet_ip[int(id)]
    write_wallet_file()

# Subfunction
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

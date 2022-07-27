#! /usr/bin/python
#---------------------------------------------

from param import param_co

import pandas as pd


def get_ip_from_key(key):
    for i in range(0, len(param_co.wallet_add)):
        if(param_co.wallet_add[i] == key):
            return param_co.wallet_ip[i]
    return "None"

def get_key_from_ip(ip):
    for i in range(0, len(param_co.wallet_add)):
        if(param_co.wallet_ip[i] == ip):
            return param_co.wallet_add[i]
    return "None"

def read_wallet():
    X = pd.read_csv('src/wallet.txt', sep=" ", header=None)
    param_co.wallet_add = list()
    param_co.wallet_ip = list()
    for i in range(0, len(X[0])):
        param_co.wallet_add.append(str(X[0][i]))
        param_co.wallet_ip.append(str(X[1][i]))

def add_new_item(new_add, new_ip):
    if(new_add != "" and new_ip != ""):
        param_co.wallet_add.append(new_add)
        param_co.wallet_ip.append(new_ip)

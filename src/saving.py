#! /usr/bin/python
#---------------------------------------------

from param import param_co

from datetime import datetime

import pandas as pd
import psutil
import os


def test_ssd_con():
    if(os.path.exists(param_co.path_ssd)):
        hdd = psutil.disk_usage(param_co.path_ssd)
        param_co.state_co["ssd"]["connected"] = True
        param_co.state_co["ssd"]["space_used"] = int(hdd.used / (2**30))
        param_co.state_co["ssd"]["space_total"] = int(hdd.total / (2**30))
    else:
        param_co.state_co["ssd"]["connected"] = False
        param_co.state_co["ssd"]["space_used"] = 0
        param_co.state_co["ssd"]["space_total"] = 0

def determine_path():
    date = get_formated_time()
    param_co.state_py["path"]["capture"] = os.path.join(param_co.path_ssd, "capture")
    param_co.state_py["path"]["name"] = param_co.state_py["path"]["additional"] + "_" + date + ".pcap"
    param_co.state_py["lidar_1"]["dir"] = os.path.join(param_co.state_py["path"]["capture"], "lidar_1")
    param_co.state_py["lidar_2"]["dir"] = os.path.join(param_co.state_py["path"]["capture"], "lidar_2")
    param_co.state_py["lidar_1"]["file"] = os.path.join(param_co.state_py["lidar_1"]["dir"], param_co.state_py["path"]["name"])
    param_co.state_py["lidar_2"]["file"] = os.path.join(param_co.state_py["lidar_2"]["dir"], param_co.state_py["path"]["name"])

def get_formated_time():
    date = datetime.now().strftime('%d-%m-%Y_%Hh%M')
    return str(date)

def read_wallet():
    X = pd.read_csv('src/wallet.txt', sep=" ", header=None)
    param_co.wallet_add = list()
    param_co.wallet_ip = list()
    for i in range(0, len(X[0])):
        param_co.wallet_add.append(str(X[0][i]))
        param_co.wallet_ip.append(str(X[1][i]))

def check_directories():
    connected = param_co.state_co["ssd"]["connected"]
    if(connected):
        # Capture directory
        path = param_co.state_py["path"]["capture"]
        if(os.path.exists(path) == False):
            create_directory(path)
        # Lidar 1 directory
        path = param_co.state_py["lidar_1"]["dir"]
        if(os.path.exists(path) == False):
            create_directory(path)
        # Lidar 2 directory
        path = param_co.state_py["lidar_2"]["dir"]
        if(os.path.exists(path) == False):
            create_directory(path)

def create_directory(path):
    os.mkdir(path)
    print("[\033[92mSSD\033[0m] Directory %s created" % path)

def clear_directory(path):
    for file in os.scandir(path):
        os.remove(file.path)

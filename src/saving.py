#! /usr/bin/python
#---------------------------------------------

from param import param_co
from classes import classes

from datetime import datetime

import pandas as pd
import psutil
import os


def test_ssd_con():
    if(os.path.exists(param_co.ssd_path)):
        param_co.ssd_connected = True
        hdd = psutil.disk_usage(param_co.ssd_path)
        param_co.ssd_space_used = int(hdd.used / (2**30))
        param_co.ssd_space_total = int(hdd.total / (2**30))
    else:
        param_co.ssd_connected = False
        param_co.ssd_space_used = 0
        param_co.ssd_space_total = 0

def determine_path():
    date = get_formated_time()
    classes.lidars.path_capture = os.path.join(param_co.ssd_path, "capture")
    classes.lidars.path_dir_l1 = os.path.join(param_co.ssd_path, "lidar_1")
    classes.lidars.path_dir_l2 = os.path.join(param_co.ssd_path, "lidar_2")
    classes.lidars.file_name = classes.lidars.path_add + "_" + date + ".pcap"
    classes.lidars.path_file_l1 = os.path.join(classes.lidars.path_dir_l1, classes.lidars.file_name)
    classes.lidars.path_file_l2 = os.path.join(classes.lidars.path_dir_l2, classes.lidars.file_name)

def get_formated_time():
    date = datetime.now().strftime('%d-%m-%Y_%Hh%M')
    return str(date)

def read_wallet():
    X = pd.read_csv('src/wallet.txt', sep=" ", header=None)
    classes.pyward.wallet_add = list()
    classes.pyward.wallet_ip = list()
    for i in range(0, len(X[0])):
        classes.pyward.wallet_add.append(str(X[0][i]))
        classes.pyward.wallet_ip.append(str(X[1][i]))

def check_directories():
    #Check existence, or create, directories
    #-------------

    # Create directory capture
    if(classes.pyward.ssd_connected):
        if(os.path.exists(classes.lidars.path_capture) == False):
            os.mkdir(classes.lidars.path_capture)
            print("[\033[92mSSD\033[0m] Directory capture created")
        # Create directory 1
        if(os.path.exists(classes.lidars.path_dir_l1) == False):
            os.mkdir(classes.lidars.path_dir_l1)
            print("[\033[92mSSD\033[0m] Directory 1 created")
        # Create directory 2
        if(os.path.exists(classes.lidars.path_dir_l2) == False):
            os.mkdir(classes.lidars.path_dir_l2)
            print("[\033[92mSSD\033[0m] Directory 2 created")

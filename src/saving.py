#! /usr/bin/python
#---------------------------------------------

from param import cla

from datetime import datetime

import pandas as pd
import psutil
import os


def test_ssd_con():
    if(os.path.exists(cla.contro.ssd_path)):
        cla.contro.ssd_connected = True
        hdd = psutil.disk_usage(cla.contro.ssd_path)
        cla.contro.ssd_space_used = int(hdd.used / (2**30))
        cla.contro.ssd_space_total = int(hdd.total / (2**30))
    else:
        cla.contro.ssd_connected = False
        cla.contro.ssd_space_used = 0
        cla.contro.ssd_space_total = 0

def determine_path():
    date = get_formated_time()
    cla.lidars.path_capture = os.path.join(cla.contro.ssd_path, "capture")
    cla.lidars.path_dir_l1 = os.path.join(cla.lidars.path_capture, "lidar_1")
    cla.lidars.path_dir_l2 = os.path.join(cla.lidars.path_capture, "lidar_2")
    cla.lidars.file_name = cla.lidars.path_add + "_" + date + ".pcap"
    cla.lidars.path_file_l1 = os.path.join(cla.lidars.path_dir_l1, cla.lidars.file_name)
    cla.lidars.path_file_l2 = os.path.join(cla.lidars.path_dir_l2, cla.lidars.file_name)

def get_formated_time():
    date = datetime.now().strftime('%d-%m-%Y_%Hh%M')
    return str(date)

def read_wallet():
    X = pd.read_csv('src/wallet.txt', sep=" ", header=None)
    cla.pyward.wallet_add = list()
    cla.pyward.wallet_ip = list()
    for i in range(0, len(X[0])):
        cla.pyward.wallet_add.append(str(X[0][i]))
        cla.pyward.wallet_ip.append(str(X[1][i]))

def check_directories():
    #Check existence, or create, directories
    #-------------

    # Create directory capture
    if(cla.pyward.ssd_connected):
        if(os.path.exists(cla.lidars.path_capture) == False):
            os.mkdir(cla.lidars.path_capture)
            print("[\033[92mSSD\033[0m] Directory capture created")
        # Create directory 1
        if(os.path.exists(cla.lidars.path_dir_l1) == False):
            os.mkdir(cla.lidars.path_dir_l1)
            print("[\033[92mSSD\033[0m] Directory 1 created")
        # Create directory 2
        if(os.path.exists(cla.lidars.path_dir_l2) == False):
            os.mkdir(cla.lidars.path_dir_l2)
            print("[\033[92mSSD\033[0m] Directory 2 created")

#---------------------------------------------
from src.param import param_co
from src.misc import terminal

from datetime import datetime

import psutil
import os


def test_ssd_con():
    path = param_co.path_ssd
    if(os.path.exists(path) and path.find("lidar_ssd") != -1):
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
    param_co.state_co["path"]["dir_capture"] = os.path.join(param_co.path_ssd, "capture")
    param_co.state_co["path"]["file_name"] = param_co.state_co["path"]["file_name_add"] + "_" + date + ".pcap"
    param_co.state_co["path"]["dir_l1"] = os.path.join(param_co.state_co["path"]["dir_capture"], "lidar_1")
    param_co.state_co["path"]["dir_l2"] = os.path.join(param_co.state_co["path"]["dir_capture"], "lidar_2")
    param_co.state_co["path"]["path_l1_file"] = os.path.join(param_co.state_co["path"]["dir_l1"], param_co.state_co["path"]["file_name"])
    param_co.state_co["path"]["path_l2_file"] = os.path.join(param_co.state_co["path"]["dir_l2"], param_co.state_co["path"]["file_name"])
    new_path = param_co.state_co["path"]["dir_capture"] + "/lidar_x/" + param_co.state_co["path"]["file_name"]

def get_formated_time():
    date = datetime.now().strftime('%d-%m-%Y_%Hh%M')
    return str(date)

def check_directories():
    connected = param_co.state_co["ssd"]["connected"]
    if(connected):
        # Capture directory
        path = param_co.state_co["path"]["dir_capture"]
        if(os.path.exists(path) == False):
            create_directory(path)
        # Lidar 1 directory
        path = param_co.state_co["path"]["dir_l1"]
        if(os.path.exists(path) == False):
            create_directory(path)
        # Lidar 2 directory
        path = param_co.state_co["path"]["dir_l2"]
        if(os.path.exists(path) == False):
            create_directory(path)

def create_directory(path):
    os.mkdir(path)
    terminal.addLog("#", "Directory %s created" % path)

def clear_directory(path):
    for file in os.scandir(path):
        os.remove(file.path)

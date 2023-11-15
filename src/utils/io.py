#---------------------------------------------
from src.param import param_control

from scapy.all import *

import os
import pcapy


def write_lidar_data(path, packet):
    activated = param_control.state_control["ssd"]["activated"]
    connected = param_control.state_control["interface"]["ssd_connected"]
    if(activated and connected and len(packet) == 1206):
        wrpcap(path, packet, append=True)

def open_pcap(path):
    pcap = scapy.utils.rdpcap(path)
    return pcap

def get_nb_paquet(pcap):
    nb = 0
    for pkt in pcap:
        if pkt.haslayer(UDP):
            nb += 1
    return nb

def get_size_Gb(path):
    if os.path.exists(path):
        size = os.path.getsize(path) / 1000000000
        return size
    else:
        return 0

def get_list_device_from_state():
    array = param_control.state_ground["device"]
    a= list()
    for key, value in array.items():
        a.append(str(value))
    return a

def write_pcap(pcap, path, is_append):
    #get file size and convert it into Gb
    if os.path.exists(path):
        size = os.path.getsize(path) / 1000000000
    else:
        size = 0

    #If the file is under 50 Gb save new pcap in file
    if size < 50:
        for pkt in pcap:
            if pkt.haslayer(UDP):
                wrpcap(path, pkt, append=is_append)  #appends packet to output file
            else:
                pass

#! /usr/bin/python
#---------------------------------------------

import psutil


def get_temps_core(number):
    temp = psutil.sensors_temperatures()
    if(temp):
        return temp["coretemp"][number+1].current

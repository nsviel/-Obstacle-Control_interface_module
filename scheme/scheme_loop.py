#---------------------------------------------
from param import param_co

import dearpygui.dearpygui as dpg


def loop():
    loop_packet()
    loop_lidar_throughput()
    loop_network()

def loop_packet():
    dpg.set_value("l1_packet", param_co.state_py["lidar_1"]["packet"]["value"])
    dpg.set_value("l2_packet", param_co.state_py["lidar_2"]["packet"]["value"])

def loop_lidar_throughput():
    # LiDAR channel 1
    dpg.set_value("l1_bdw_val", param_co.state_py["lidar_1"]["throughput"]["value"])
    min = param_co.state_py["lidar_1"]["throughput"]["min"]
    mean = param_co.state_py["lidar_1"]["throughput"]["mean"]
    max = param_co.state_py["lidar_1"]["throughput"]["max"]
    bandwidth = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("l1_bdw_range", bandwidth)

    # LiDAR channel 2
    dpg.set_value("l2_bdw_val", param_co.state_py["lidar_2"]["throughput"]["value"])
    min = param_co.state_py["lidar_2"]["throughput"]["min"]
    mean = param_co.state_py["lidar_2"]["throughput"]["mean"]
    max = param_co.state_py["lidar_2"]["throughput"]["max"]
    bandwidth = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("l2_bdw_range", bandwidth)

def loop_network():
    # LiDAR channel 1
    dpg.set_value("l1_bdw_val", param_co.state_py["lidar_1"]["throughput"]["value"])
    min = param_co.state_py["lidar_1"]["throughput"]["min"]
    mean = param_co.state_py["lidar_1"]["throughput"]["mean"]
    max = param_co.state_py["lidar_1"]["throughput"]["max"]
    bandwidth = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("l1_bdw_range", bandwidth)

    # LiDAR channel 2
    dpg.set_value("l2_bdw_val", param_co.state_py["lidar_2"]["throughput"]["value"])
    min = param_co.state_py["lidar_2"]["throughput"]["min"]
    mean = param_co.state_py["lidar_2"]["throughput"]["mean"]
    max = param_co.state_py["lidar_2"]["throughput"]["max"]
    bandwidth = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("l2_bdw_range", bandwidth)

    # Network KPIs
    dpg.set_value("net_l1_bandwidth_val", param_co.state_perf["local_cloud"]["bandwidth"]["value"])
    min = param_co.state_perf["local_cloud"]["bandwidth"]["min"]
    mean = param_co.state_perf["local_cloud"]["bandwidth"]["mean"]
    max = param_co.state_perf["local_cloud"]["bandwidth"]["max"]
    bandwidth = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("net_l1_bandwidth_range", bandwidth)

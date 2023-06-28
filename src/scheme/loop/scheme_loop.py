#---------------------------------------------
from src.param import param_interface

import dearpygui.dearpygui as dpg


def loop():
    loop_packet()
    loop_lidar_throughput()
    loop_perf()

def loop_packet():
    dpg.set_value("l1_packet", param_interface.state_capture["lidar_1"]["packet"]["value"])
    dpg.set_value("l2_packet", param_interface.state_capture["lidar_2"]["packet"]["value"])

def loop_lidar_throughput():
    # LiDAR channel 1
    value = "%.2f"% param_interface.state_capture["lidar_1"]["throughput"]["value"]
    min = param_interface.state_capture["lidar_1"]["throughput"]["min"]
    mean = param_interface.state_capture["lidar_1"]["throughput"]["mean"]
    max = param_interface.state_capture["lidar_1"]["throughput"]["max"]
    range = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("l1_tgp_val", value)
    dpg.set_value("l1_tgp_range", range)

    # LiDAR channel 2
    value = "%.3f"% param_interface.state_capture["lidar_2"]["throughput"]["value"]
    min = param_interface.state_capture["lidar_2"]["throughput"]["min"]
    mean = param_interface.state_capture["lidar_2"]["throughput"]["mean"]
    max = param_interface.state_capture["lidar_2"]["throughput"]["max"]
    range = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("l2_tgp_val", value)
    dpg.set_value("l2_tgp_range", range)

def loop_perf():
    # Throughput
    value = "%.2f"% param_interface.state_capture[param_interface.lidar_main]["throughput"]["value"]
    dpg.set_value("perf_throughput_up_val", value)

    # Latency
    value = "%.2f"% param_interface.state_network["local_cloud"]["latency"]["value"]
    dpg.set_value("perf_latency_up_val", value)
    value = "%.2f"% param_interface.state_network["cloud_local"]["latency"]["value"]
    dpg.set_value("perf_latency_do_val", value)

    # Reliability
    value = "%.2f"% param_interface.state_network["local_cloud"]["reliability"]["value"]
    dpg.set_value("perf_reliability_up_val", value)
    value = "%.2f"% param_interface.state_network["cloud_local"]["reliability"]["value"]
    dpg.set_value("perf_reliability_do_val", value)

    # Interruption time
    value = "%.2f"% param_interface.state_network["local_cloud"]["interruption"]["value"]
    dpg.set_value("perf_interruption_val", value)

    # End to end time
    #dpg.set_value("perf_time_slam", param_interface.state_network["end_to_end"]["time_slam"])
    #dpg.set_value("perf_time_ai", param_interface.state_network["end_to_end"]["time_ai"])
    dpg.set_value("perf_time_total", param_interface.state_network["end_to_end"]["time_total"])

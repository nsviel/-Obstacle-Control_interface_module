#---------------------------------------------
from src.param import param_co

import dearpygui.dearpygui as dpg


def loop():
    loop_packet()
    loop_lidar_throughput()
    loop_perf()

def loop_packet():
    dpg.set_value("l1_packet", param_co.state_py["lidar_1"]["packet"]["value"])
    dpg.set_value("l2_packet", param_co.state_py["lidar_2"]["packet"]["value"])

def loop_lidar_throughput():
    # LiDAR channel 1
    value = "%.2f"% param_co.state_py["lidar_1"]["throughput"]["value"]
    min = param_co.state_py["lidar_1"]["throughput"]["min"]
    mean = param_co.state_py["lidar_1"]["throughput"]["mean"]
    max = param_co.state_py["lidar_1"]["throughput"]["max"]
    range = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("l1_tgp_val", value)
    dpg.set_value("l1_tgp_range", range)

    # LiDAR channel 2
    value = "%.3f"% param_co.state_py["lidar_2"]["throughput"]["value"]
    min = param_co.state_py["lidar_2"]["throughput"]["min"]
    mean = param_co.state_py["lidar_2"]["throughput"]["mean"]
    max = param_co.state_py["lidar_2"]["throughput"]["max"]
    range = "%.2f, %.2f, %.2f"% (min, mean, max)
    dpg.set_value("l2_tgp_val", value)
    dpg.set_value("l2_tgp_range", range)

def loop_perf():
    # Bandwidth
    #value = "%.2f"% param_co.state_perf["local_cloud"]["throughput"]["value"]
    #dpg.set_value("perf_bandwidth_up_val", value)
    #value = "%.2f"% param_co.state_perf["cloud_local"]["throughput"]["value"]
    #dpg.set_value("perf_bandwidth_do_val", value)

    # Throughput
    value = "%.2f"% param_co.state_py[param_co.lidar_main]["throughput"]["value"]
    dpg.set_value("perf_throughput_up_val", value)

    # Latency
    value = "%.2f"% param_co.state_perf["local_cloud"]["latency"]["value"]
    dpg.set_value("perf_latency_up_val", value)
    value = "%.2f"% param_co.state_perf["cloud_local"]["latency"]["value"]
    dpg.set_value("perf_latency_do_val", value)

    # Jitter
    #value = "%.3f"% param_co.state_perf["local_cloud"]["jitter"]["value"]
    #dpg.set_value("perf_jitter_up_val", value)
    #value = "%.3f"% param_co.state_perf["cloud_local"]["jitter"]["value"]
    #dpg.set_value("perf_jitter_do_val", value)

    # Reliability
    value = "%.2f"% param_co.state_perf["local_cloud"]["reliability"]["value"]
    dpg.set_value("perf_reliability_up_val", value)
    #value = "%.2f"% param_co.state_perf["cloud_local"]["reliability"]["value"]
    #dpg.set_value("perf_reliability_do_val", value)

    # Interruption time
    value = "%.2f"% param_co.state_perf["local_cloud"]["interruption"]["value"]
    dpg.set_value("perf_interruption_val", value)

    # End to end time
    #dpg.set_value("perf_time_slam", param_co.state_perf["end_to_end"]["time_slam"])
    #dpg.set_value("perf_time_ai", param_co.state_perf["end_to_end"]["time_ai"])
    dpg.set_value("perf_time_total", param_co.state_perf["end_to_end"]["time_total"])

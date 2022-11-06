#---------------------------------------------
from param import param_co

import dearpygui.dearpygui as dpg

color_info = (0, 200, 200)
color_grey = (150, 150, 150)


def module_network():
    with dpg.table(header_row=True, borders_innerH=True, width=300):

        dpg.add_table_column()
        dpg.add_table_column(label="Upload")
        dpg.add_table_column(label="Download")

        add_perf_bandwidth("perf_bandwidth_up_val", "perf_bandwidth_up_range", "perf_bandwidth_do_val", "perf_bandwidth_do_range")
        add_perf_latency("perf_latency_up_val", "perf_latency_up_range", "perf_latency_do_val", "perf_latency_do_range")
        #add_perf_jitter("perf_jitter_up_val", "perf_jitter_up_range", "perf_jitter_do_val", "perf_jitter_do_range")
        add_perf_reliability("perf_reliability_up_val", "perf_reliability_up_range", "perf_reliability_do_val", "perf_reliability_do_range")
        add_perf_interruption("perf_interruption_val", "perf_interruption_range")

    with dpg.table(header_row=True, borders_innerH=True):

        dpg.add_table_column()
        dpg.add_table_column(label="End-to-end")

        add_perf_time("Time SLAM", "perf_time_slam")
        add_perf_time("Time AI", "perf_time_ai")
        add_perf_time("Time total", "perf_time_total")

# Perf stuff
def add_perf_bandwidth(tag_val_up, tag_range_up, tag_val_do, tag_range_do):
    with dpg.table_row():
        dpg.add_text("Bandwidth")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("MB/s");
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_do, color=color_info);
            dpg.add_text("MB/s");
def add_perf_latency(tag_val_up, tag_range_up, tag_val_do, tag_range_do):
    with dpg.table_row():
        dpg.add_text("Latency")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("ms");
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_do, color=color_info);
            dpg.add_text("ms");
def add_perf_jitter(tag_val_up, tag_range_up, tag_val_do, tag_range_do):
    with dpg.table_row():
        dpg.add_text("Jitter")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("ms");
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_do, color=color_info);
            dpg.add_text("ms");
def add_perf_reliability(tag_val_up, tag_range_up, tag_val_do, tag_range_do):
    with dpg.table_row():
        dpg.add_text("Reliability")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("%");
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_do, color=color_info);
            dpg.add_text("%");
def add_perf_interruption(tag_val, tag_range):
    with dpg.table_row():
        dpg.add_text("Interruption")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val, color=color_info);
            dpg.add_text("ms");

def add_perf_time(text, tag):
    with dpg.table_row():
        dpg.add_text(text)
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag, color=color_info);
            dpg.add_text("ms");

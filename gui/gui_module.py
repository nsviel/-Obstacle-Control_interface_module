#---------------------------------------------
from param import param_co
from gui import gui_callback

import dearpygui.dearpygui as dpg

color_info = (0, 200, 200)
color_grey = (150, 150, 150)


def module_network():
    with dpg.group(horizontal=True):
        dpg.add_image("icon_wifi")
        #dpg.add_checkbox(tag="iperf_activated", label="With iperf", default_value=True, callback=gui_callback.callback_with_iperf)
    with dpg.table(header_row=True, borders_innerH=True, width=350):
        dpg.add_table_column()
        dpg.add_table_column(label="Upload")
        dpg.add_table_column(label="Download")
        dpg.add_table_column(label="Required")

        add_perf_throughput("perf_throughput_up_val")
        #add_perf_bandwidth("perf_bandwidth_up_val", "perf_bandwidth_do_val")
        add_perf_latency("perf_latency_up_val", "perf_latency_do_val")
        #add_perf_jitter("perf_jitter_up_val", "perf_jitter_do_val")
        add_perf_reliability("perf_reliability_up_val")
        add_perf_interruption("perf_interruption_val")

    with dpg.table(header_row=True, borders_innerH=True):

        dpg.add_table_column()
        dpg.add_table_column(label="Time")
        dpg.add_table_column(label="Required")

        #add_perf_time("SLAM", "perf_time_slam")
        #add_perf_time("AI", "perf_time_ai")
        add_perf_time_total("End-to-end", "perf_time_total")

# Perf stuff
def add_perf_bandwidth(tag_val_up, tag_val_do):
    with dpg.table_row():
        dpg.add_text("Bandwidth")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("Mb/s");
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_do, color=color_info);
            dpg.add_text("Mb/s");
        dpg.add_text("[5, 20] Mb/s");
def add_perf_throughput(tag_val_up):
    with dpg.table_row():
        dpg.add_text("Throughput")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("Mb/s");
        dpg.add_text("");
        dpg.add_text("[5, 20] Mb/s");
def add_perf_latency(tag_val_up, tag_val_do):
    with dpg.table_row():
        dpg.add_text("Latency")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("ms");
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_do, color=color_info);
            dpg.add_text("ms");
        dpg.add_text("< 200 ms");
def add_perf_jitter(tag_val_up, tag_val_do):
    with dpg.table_row():
        dpg.add_text("Jitter")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("ms");
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_do, color=color_info);
            dpg.add_text("ms");
def add_perf_reliability(tag_val_up):
    with dpg.table_row():
        dpg.add_text("Reliability")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("%");
        dpg.add_text("");
        dpg.add_text(">= 99 %");
def add_perf_interruption(tag_val):
    with dpg.table_row():
        dpg.add_text("Interruption")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val, color=color_info);
            dpg.add_text("s");
        dpg.add_text("");
        dpg.add_text("< 1 s");

def add_perf_time(text, tag):
    with dpg.table_row():
            dpg.add_text(text)
            with dpg.group(horizontal=True):
                dpg.add_text(0, tag=tag, color=color_info);
                dpg.add_text("ms");
def add_perf_time_total(text, tag):
    with dpg.table_row():
        dpg.add_text(text)
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag, color=color_info);
            dpg.add_text("ms")
        dpg.add_text("[1.6, 2] s");

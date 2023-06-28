#---------------------------------------------
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="SSD", tag="node_ssd"):
        scheme_function.add_status_i("ssd_input", "ssd_status_but", "ssd_status")
        scheme_function.add_ssd_active("ssd_active")
        scheme_function.add_ssd_param("ssd_path", "file_name", "ssd_path_add", "ssd_used", "ssd_total", "ssd_param_visible")
        scheme_function.add_file_info("Lidar 1", "l1_file_path", "l1_file_size", "ssd_l1_visible")
        scheme_function.add_file_info("Lidar 2", "l2_file_path", "l2_file_size", "ssd_l2_visible")

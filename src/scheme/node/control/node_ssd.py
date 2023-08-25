#---------------------------------------------
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="SSD", tag="node_ssd"):
        scheme_function.add_status_i("ssd_input", object.object.ssd.ID_status_light, object.object.ssd.ID_status)
        scheme_function.add_ssd_active(object.object.ssd.ID_activated)
        scheme_function.add_ssd_param(object.object.ssd.ID_path, object.object.ssd.ID_file_name, object.object.ssd.ID_path_add, object.object.ssd.ID_memory_used, object.object.ssd.ID_memory_total, object.object.ssd.ID_parameter_visibility)
        scheme_function.add_file_info("Lidar 1", object.object.ssd.ID_path_l1, object.object.ssd.ID_file_l1_size, object.object.ssd.ID_path_l1_visibility)
        scheme_function.add_file_info("Lidar 2", object.object.ssd.ID_path_l2, object.object.ssd.ID_file_l2_size, object.object.ssd.ID_path_l2_visibility)

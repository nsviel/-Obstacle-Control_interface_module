#---------------------------------------------
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_block():
    with dpg.node(label="Train", tag="node_block_train"):
        scheme_function.add_image("icon_train", "icon_train_visible")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.drawlist(tag="block_train", width=450, height=200):
                pass

def design_node():
    with dpg.node(label="LiDAR", tag="node_train"):
        scheme_function.add_image("icon_lidar", "icon_lidar_visible")
        scheme_function.add_geolocalization("geo_status", "geo_country")

        scheme_function.line_tagged("l1_line_visible")
        scheme_function.add_lidar_status("Lidar 1", "l1_status", "l1_activated", "l1_status_but")
        scheme_function.add_l1_motor("l1_on", "l1_off", "l1_motor_visible")
        scheme_function.add_lidar_add("l1_wallet", "l1_ip", "l1_params_visible")
        scheme_function.add_port_lidar("l1_port", "l1_port_visible")
        scheme_function.add_l1_speed("l1_speed", "l1_speedge_2_visible")
        scheme_function.add_lidar_stat("l1_packet", "l1_tgp_val", "l1_tgp_range", "l1_perf_visible")

        scheme_function.line_tagged("l2_line_visible")
        scheme_function.add_lidar_status("Lidar 2", "l2_status", "l2_activated", "l2_status_but")
        scheme_function.add_l2_motor("l2_on", "l2_off", "l2_motor_visible")
        scheme_function.add_lidar_add("l2_wallet", "l2_ip", "l2_params_visible")
        scheme_function.add_port_lidar("l2_port", "l2_port_visible")
        scheme_function.add_l2_speed("l2_speed", "l2_speedge_2_visible")
        scheme_function.add_lidar_stat("l2_packet", "l2_tgp_val", "l2_tgp_range", "l2_perf_visible")

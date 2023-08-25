#---------------------------------------------
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def design_block():
    with dpg.node(label="Train", tag="node_block_train"):
        scheme_function.add_image("icon_train", "icon_train_visible")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.drawlist(tag="block_train", width=450, height=200):
                pass

def design_node():
    with dpg.node(label="LiDAR", tag="node_train"):
        scheme_function.add_image("icon_lidar", object.object.train.ID_icon_lidar_visibility)

        scheme_function.add_lidar_status("Lidar 1", object.object.train.ID_l1_status, object.object.train.ID_l1_activated, object.object.train.ID_l1_status_light)
        scheme_function.add_l1_motor(object.object.train.ID_l1_motor_on, object.object.train.ID_l1_motor_off, object.object.train.ID_l1_motor_visibility)
        scheme_function.add_lidar_add(object.object.train.ID_l1_wallet, object.object.train.ID_l1_ip, object.object.train.ID_l1_ip_visibility)
        scheme_function.add_port_lidar(object.object.train.ID_l1_sock_client_port, object.object.train.ID_l1_sock_client_port_visibility)
        scheme_function.add_l1_speed(object.object.train.ID_l1_motor_speed, object.object.train.ID_l1_motor_speed_visibility)
        scheme_function.add_lidar_stat(object.object.train.ID_l1_stat_packet, object.object.train.ID_l1_throughtput_value, object.object.train.ID_l1_throughtput_range, object.object.train.ID_l1_stat_visibility)

        scheme_function.line_tagged(object.object.train.ID_l2_line_visibility)
        scheme_function.add_lidar_status("Lidar 2", object.object.train.ID_l2_status, object.object.train.ID_l2_activated, object.object.train.ID_l2_status_light)
        scheme_function.add_l2_motor(object.object.train.ID_l2_motor_on, object.object.train.ID_l2_motor_off, object.object.train.ID_l2_motor_visibility)
        scheme_function.add_lidar_add(object.object.train.ID_l2_wallet, object.object.train.ID_l2_ip, object.object.train.ID_l2_ip_visibility)
        scheme_function.add_port_lidar(object.object.train.ID_l2_sock_client_port, object.object.train.ID_l2_sock_client_port_visibility)
        scheme_function.add_l2_speed(object.object.train.ID_l2_motor_speed, object.object.train.ID_l2_motor_speed_visibility)
        scheme_function.add_lidar_stat(object.object.train.ID_l2_stat_packet, object.object.train.ID_l2_throughtput_value, object.object.train.ID_l2_throughtput_range, object.object.train.ID_l2_stat_visibility)

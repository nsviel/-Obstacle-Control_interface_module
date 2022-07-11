#! /usr/bin/python
#---------------------------------------------

from scheme import scheme_function
from scheme import scheme_connection
from scheme import scheme_callback

import dearpygui.dearpygui as dpg

coord_controlium = [375, 500]
coord_pywardium = [350, 10]
coord_hubium = [700, 250]
coord_train = [10, 10]
coord_edge = [1000, 500]
coord_local = [1000, 10]
coord_sncf = [1000, 175]
coord_valeo = [1000, 350]
coord_ssd = [10, 500]
coord_image = [600, 10]


def node_controlium():
    with dpg.node(label="Controlium", tag="node_co", pos=coord_controlium):
        scheme_function.add_status("co_status")
        scheme_function.add_ip("co_ip")

        scheme_function.add_input("self", "co_self")

        scheme_connection.add_http_client_o("co_http_client")
        scheme_function.add_false_alarm()
        scheme_function.add_choice_edge()

        scheme_connection.add_sock_server_o("co_sock_server")
        scheme_function.add_port("co_sock_server_port")

def node_pywardium():
    with dpg.node(label="Pywardium", tag="node_py", pos=coord_pywardium):
        scheme_function.add_status("py_status")
        scheme_function.add_ip("py_ip")

        scheme_function.add_input("self", "py_self")
        scheme_function.add_lidar_device("Lidar 1", ("a", "b"), "a", "py_l1_device", "py_l1_device_port")
        scheme_function.add_lidar_device("Lidar 2", ("a", "b"), "a", "py_l2_device", "py_l2_device_port")

        scheme_connection.add_sock_client_o("py_sock_client")
        scheme_function.add_port("py_sock_client_port")

        scheme_connection.add_http_server_o("py_http_server")
        scheme_function.add_port("py_http_server_port")

def node_hubium():
    with dpg.node(label="Hubium", tag="node_hu", pos=coord_hubium):
        scheme_function.add_status("hu_status")
        scheme_function.add_ip("hu_ip")

        scheme_function.add_stockage("hu_stockage")
        scheme_function.add_mqtt("hu_mqtt")

        scheme_connection.add_sock_client_io("hu_sock_client_i", "hu_sock_client_o")
        scheme_function.add_port("hu_sock_client_port")

        scheme_connection.add_sock_server_io("hu_sock_server_i", "hu_sock_server_o")
        scheme_function.add_port("hu_sock_server_port")

        scheme_connection.add_http_client_io("hu_http_client_i", "hu_http_client_o")
        scheme_function.add_port("hu_http_client_port")

        scheme_connection.add_http_server_io("hu_http_server_i", "hu_http_server_o")
        scheme_function.add_port("hu_http_server_port")

def node_train():
    with dpg.node(label="Train", tag="node_train", pos=coord_train):
        scheme_function.add_geolocalization("geo_country")
        scheme_function.add_lidar("Lidar 1", "l1_input", "l1_active", "l1_speed", "l1_ip", "l1_packet")
        scheme_function.add_lidar("Lidar 2", "l2_input", "l2_active", "l2_speed", "l2_ip", "l2_packet")
        scheme_function.add_variable("Time:", "capture_time")

def node_edge():
    with dpg.node(label="Edge", tag="node_ed", pos=coord_edge):
        scheme_function.add_status("ed_status")
        scheme_function.add_ip("ed_ip")

        scheme_connection.add_sock_client_i("ed_sock_client")
        scheme_function.add_port("ed_sock_client_port")

        scheme_connection.add_sock_server_i("ed_sock_server")
        scheme_function.add_port("ed_sock_server_port")

        scheme_connection.add_http_server_i("ed_http_server")
        scheme_function.add_port("ed_http_server_port")

def node_edge_local():
    with dpg.node(label="Local", tag="node_local", pos=coord_local):
        scheme_function.add_attribute("Velodium")
        scheme_connection.add_sock_server_i("ve_sock_server")
        scheme_function.add_port("ve_sock_server_port")

        scheme_function.add_input("AI", "ai_input")

def node_sncf():
    with dpg.node(label="SNCF", tag="node_sncf", pos=coord_sncf):
        scheme_function.add_ip("sncf_ip")

        scheme_function.add_input("MQTT", "sncf_mqtt_broker")
        scheme_function.add_topic("sncf_mqtt_topic")
        scheme_function.add_port("sncf_mqtt_port")

def node_valeo():
    with dpg.node(label="Valeo", tag="node_valeo", pos=coord_valeo):
        scheme_function.add_ip("va_ip")
        scheme_connection.add_http_client_i("va_http_client")

def node_ssd():
    with dpg.node(label="SSD", tag="node_ssd", pos=coord_ssd):
        scheme_function.add_ssd("ssd_input", "ssd_active", "ssd_path", "file_name", "ssd_path_add", "ssd_used", "ssd_total")
        scheme_function.add_file_info("Lidar 1", "l1_file_path", "l1_file_size")
        scheme_function.add_file_info("Lidar 2", "l2_file_path", "l2_file_size")

def node_image():
    with dpg.node(label="Image", tag="node_image", pos=coord_image):
        scheme_function.add_image("image_in")

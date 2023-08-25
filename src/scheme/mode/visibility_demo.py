#---------------------------------------------
from src.param import param_interface
from src.connection.HTTPS import https_client_get
from src.connection.HTTPS import https_client_post
from src.scheme.loop import scheme_update
from src.scheme.mode import mode_position
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def set_visibility():
    visibility_train()
    visibility_capture()
    visibility_control()
    visibility_cloud()
    visibility_info()
    visibility_edge_1()
    visibility_edge_2()
    visibility_lidar()
    visibility_node()
    visibility_link()

def visibility_train():
    dpg.show_item(object.object.train.ID_icon_lidar_visibility)
    dpg.hide_item(object.object.train.ID_l1_ip_visibility)
    dpg.hide_item(object.object.train.ID_l1_motor_speed_visibility)
    dpg.hide_item(object.object.train.ID_l1_sock_client_port_visibility)
    dpg.hide_item(object.object.train.ID_l2_line_visibility)
    dpg.hide_item(object.object.train.ID_l2_ip_visibility)
    dpg.hide_item(object.object.train.ID_l2_motor_speed_visibility)
    dpg.hide_item(object.object.train.ID_l2_sock_client_port_visibility)
def visibility_capture():
    dpg.hide_item(object.object.capture.ID_ip_visibility)
    dpg.hide_item(object.object.capture.ID_thread_visibility)
    dpg.hide_item(object.object.capture.ID_http_server_port_visibility)
    dpg.hide_item(object.object.capture.ID_sock_server_l1_port_visibility)
    dpg.hide_item(object.object.capture.ID_sock_server_l2_port_visibility)
    dpg.hide_item(object.object.capture.ID_device_visibility)
def visibility_control():
    dpg.hide_item(object.object.control.ID_temperature_visibility)
    dpg.hide_item(object.object.control.ID_sock_server_l1_port_visibility)
    dpg.hide_item(object.object.control.ID_sock_server_l2_port_visibility)
def visibility_cloud():
    dpg.hide_item(object.object.operator.ID_mqtt_broker_port_visibility)
    dpg.hide_item(object.object.operator.ID_mqtt_topic_visibility)
    dpg.hide_item(object.object.operator.ID_ip_visibility)
def visibility_info():
    dpg.configure_viewport("viewport", title="System control interface")
    dpg.show_item("icon_computer_visible")
    dpg.hide_item("l2_plot_visible")
    dpg.hide_item("table_mongo")
    dpg.hide_item("ID_nb_prediction_visibility")
    dpg.hide_item("ID_nb_frame_visibility")
def visibility_edge_1():
    dpg.show_item(object.object.edge_1.ID_ip_visibility)
    dpg.hide_item(object.object.edge_1.ID_thread_visibility)
    dpg.hide_item(object.object.edge_1.ID_source_1)
    dpg.hide_item(object.object.edge_1.ID_source_2)
    dpg.hide_item(object.object.edge_1.ID_http_server_port_visibility)
    dpg.hide_item(object.object.edge_1.ID_http_server_o)
    dpg.hide_item(object.object.edge_1.ID_http_client_o)
    dpg.hide_item(object.object.edge_1.ID_sock_client_l1_lidar_main)
    dpg.hide_item(object.object.edge_1.ID_sock_client_l1_i)
    dpg.hide_item(object.object.edge_1.ID_sock_client_l1_o)
    dpg.hide_item(object.object.edge_1.ID_sock_server_l1_port_visibility)
    dpg.hide_item(object.object.edge_1.ID_sock_client_l2_source)
    dpg.hide_item(object.object.edge_1.ID_sock_server_l2_port_visibility)
    dpg.show_item(object.object.edge_1.ID_sock_client_l2_o)
    dpg.hide_item(object.object.edge_1.ID_mqtt_visibility)
def visibility_edge_2():
    #dpg.hide_item(object.object.edge_2.ID_ip_visibility)
    dpg.hide_item(object.object.edge_2.ID_thread_visibility)

def visibility_lidar():
    if(param_interface.lidar_main == "lidar_1"):
        dpg.show_item(object.object.train.ID_l1_status)
        dpg.show_item(object.object.train.ID_l1_motor_visibility)
        dpg.show_item(object.object.train.ID_l1_stat_visibility)
        dpg.hide_item(object.object.train.ID_l2_status)
        dpg.hide_item(object.object.train.ID_l2_motor_visibility)
        dpg.hide_item(object.object.train.ID_l2_stat_visibility)

        dpg.hide_item(object.object.capture.ID_sock_server_l2)
        dpg.hide_item(object.object.capture.ID_sock_client_l2)
        dpg.show_item(object.object.capture.ID_sock_server_l1)

        dpg.show_item(object.object.edge_1.ID_sock_server_l1_i)
        dpg.hide_item(object.object.edge_1.ID_sock_server_l2_i)
        dpg.hide_item(object.object.edge_1.ID_sock_client_l2_o)

        dpg.show_item(object.object.edge_2.ID_sock_server_l1_i)
        dpg.hide_item(object.object.edge_2.ID_sock_server_l2_i)
        dpg.hide_item(object.object.edge_2.ID_sock_client_l2_o)

        dpg.show_item("link_l1_py")
        dpg.hide_item("link_l2_py")
        dpg.show_item("link_capture_edge_1_l1_sock")
        dpg.hide_item("link_capture_edge_1_l2_sock")
    if(param_interface.lidar_main == "lidar_2"):
        dpg.show_item(object.object.train.ID_l2_status)
        dpg.show_item(object.object.train.ID_l2_motor_visibility)
        dpg.show_item(object.object.train.ID_l2_stat_visibility)
        dpg.hide_item(object.object.train.ID_l1_status)
        dpg.hide_item(object.object.train.ID_l1_motor_visibility)
        dpg.hide_item(object.object.train.ID_l1_stat_visibility)

        dpg.show_item(object.object.capture.ID_sock_server_l2)
        dpg.hide_item(object.object.capture.ID_sock_server_l1)
        dpg.hide_item(object.object.capture.ID_sock_client_l1)

        dpg.show_item(object.object.edge_1.ID_sock_server_l2_i)
        dpg.show_item(object.object.edge_1.ID_sock_client_l2_o)
        dpg.hide_item(object.object.edge_1.ID_sock_server_l1_i)

        dpg.show_item(object.object.edge_2.ID_sock_server_l2_i)
        dpg.show_item(object.object.edge_2.ID_sock_client_l2_o)
        dpg.hide_item(object.object.edge_2.ID_sock_server_l1_i)

        dpg.hide_item("link_l1_py")
        dpg.show_item("link_l2_py")
        dpg.hide_item("link_capture_edge_1_l1_sock")
        dpg.show_item("link_capture_edge_1_l2_sock")
def visibility_node():
    dpg.show_item("node_block_train")
    dpg.show_item("node_block_edge")
    dpg.show_item("node_block_cloud")
    dpg.show_item("node_capture")
    dpg.show_item(object.object.edge_1.ID_node)
    dpg.show_item(object.object.edge_2.ID_node)
    dpg.show_item("node_data")
    dpg.show_item("node_operator")
    dpg.show_item("node_train")
    dpg.hide_item("node_slam")
    dpg.hide_item("node_ai")
    dpg.hide_item("node_ssd")
    dpg.hide_item("node_cloud_car")
    dpg.hide_item("node_control")
def visibility_link():
    dpg.hide_item("link_control_ssd_usb")
    dpg.hide_item("link_edge_1_interface_l1_sock")
    dpg.hide_item("link_edge_1_interface_l2_sock")
    dpg.hide_item("link_edge_1_car_http")
    dpg.hide_item("link_edge_1_processing_http")
    dpg.hide_item("link_edge_1_processing_sock")
    dpg.hide_item("link_edge_1_ai_http")
    dpg.hide_item("link_edge_1_control_http")
    dpg.hide_item("link_edge_2_ai_http")
    dpg.hide_item("link_edge_2_processing_http")

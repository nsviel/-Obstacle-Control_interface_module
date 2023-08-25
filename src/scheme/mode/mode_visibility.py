#---------------------------------------------
from src.param import param_interface
from src.connection.HTTPS import https_client_get
from src.connection.HTTPS import https_client_post
from src.connection.SOCK import sock_server
from src.scheme.loop import scheme_update
from src.scheme.mode import mode_position
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def set_mode_dev():
    # Block
    dpg.hide_item("node_block_train")
    dpg.hide_item("node_block_edge")
    dpg.hide_item("node_block_cloud")

    # Icon
    dpg.hide_item(object.train.ID_icon_lidar_visibility)
    dpg.hide_item("icon_computer_visible")

    # Misc
    dpg.show_item(object.control.ID_temperature_visibility)
    dpg.show_item(object.operator.ID_mqtt_broker_port_visibility)
    dpg.show_item(object.edge_1.ID_mqtt_visibility)
    dpg.show_item(object.operator.ID_mqtt_topic_visibility)
    #dpg.show_item(object.edge_1.ID_ip_visibility)
    dpg.show_item(object.train.ID_geoloc_status)
    dpg.show_item("l2_plot_visible")

    # IP
    #dpg.show_item(object.edge_1.ID_ip_visibility)
    dpg.show_item(object.capture.ID_ip_visibility)
    dpg.show_item(object.operator.ID_ip_visibility)

    # Mongo
    dpg.show_item("table_mongo")

    # LiDARs
    dpg.show_item(object.train.ID_l1_status)
    dpg.show_item(object.train.ID_l1_motor_visibility)
    dpg.show_item(object.train.ID_l1_stat_visibility)
    dpg.show_item("link_l1_py")
    dpg.show_item(object.capture.ID_sock_server_l1)
    dpg.show_item(object.capture.ID_sock_client_l1)
    dpg.show_item(object.edge_1.ID_sock_client_l1_o)
    dpg.show_item(object.edge_1.ID_sock_server_l1_i)
    dpg.show_item("link_capture_edge_l1_sock")
    dpg.show_item(object.edge_1.ID_sock_client_l1_i)
    dpg.show_item(object.train.ID_l1_line_visibility)
    dpg.show_item(object.train.ID_l1_ip_visibility)
    dpg.show_item(object.train.ID_l1_motor_speed_visibility)
    dpg.show_item(object.train.ID_l1_sock_client_port_visibility)
    dpg.show_item(object.edge_1.ID_source_1)
    dpg.show_item(object.edge_1.ID_source_2)
    dpg.show_item(object.train.ID_l2_line_visibility)
    dpg.show_item(object.train.ID_l2_ip_visibility)
    dpg.show_item(object.train.ID_l2_motor_speed_visibility)
    dpg.show_item(object.edge_1.ID_sock_client_l2_source)
    dpg.show_item(object.train.ID_l2_sock_client_port_visibility)
    dpg.show_item(object.edge_1.ID_sock_client_l2_o)
    dpg.show_item(object.train.ID_l2_status)
    dpg.show_item(object.train.ID_l2_motor_visibility)
    dpg.show_item(object.train.ID_l2_stat_visibility)
    dpg.show_item("link_l2_py")
    dpg.show_item(object.capture.ID_sock_server_l2)
    dpg.show_item(object.capture.ID_sock_client_l2)
    dpg.show_item(object.edge_1.ID_sock_server_l2_i)
    dpg.show_item("link_capture_edge_l2_sock")

    # SSD
    dpg.show_item(object.ssd.ID_parameter_visibility)
    dpg.show_item(object.ssd.ID_path_l1_visibility)
    dpg.show_item(object.ssd.ID_path_l2_visibility)

    # Nodes
    dpg.show_item("node_slam")
    dpg.show_item("node_ai")
    dpg.show_item("node_edge_2")
    dpg.show_item("node_ssd")
    dpg.show_item("node_cloud_car")
    dpg.show_item("node_control")
    dpg.configure_viewport("viewport", title="module_interface")

    # Links
    dpg.show_item("link_l2_py")
    dpg.show_item("link_va_hu")
    dpg.show_item("link_ai_edge_1_http")
    #dpg.show_item("link_edge_2_edge_1_http")
    #dpg.show_item("link_edge_2_edge_sock")
    #dpg.show_item("link_edge_edge_2_sock")
    #dpg.show_item("link_edge_edge_2_http")
    dpg.show_item("link_edge_interface_l1_sock")
    dpg.show_item("link_edge_interface_l2_sock")
    dpg.show_item("link_edge_processing_http")
    dpg.show_item("link_edge_processing_sock")

    #dpg.show_item("link_edge_2_edge_sock")
    #dpg.show_item("link_edge_2_edge_1_http")
    dpg.show_item("link_capture_geo")
    dpg.show_item("link_capture_edge_l2_sock")
    dpg.show_item("link_interface_edge_1_http")
    dpg.show_item("link_interface_ssd")

    # Nb threads
    dpg.show_item(object.control.ID_thread_visibility)
    dpg.show_item(object.edge_1.ID_thread_visibility)
    dpg.show_item(object.capture.ID_thread_visibility)

    # HTTP ports
    dpg.show_item(object.capture.ID_http_server_port_visibility)
    dpg.show_item(object.edge_1.ID_http_server_port_visibility)
    #dpg.show_item("edge_2_http_port_visible")
    dpg.show_item(object.edge_1.ID_http_server_o)
    dpg.show_item(object.edge_1.ID_http_client_o)

    # Socket ports
    dpg.show_item(object.control.ID_sock_server_l1_port_visibility)
    dpg.show_item(object.control.ID_sock_server_l2_port_visibility)
    dpg.show_item(object.edge_1.ID_sock_server_l1_port_visibility)
    dpg.show_item(object.edge_1.ID_sock_server_l2_port_visibility)
    dpg.show_item(object.capture.ID_sock_server_l1_port_visibility)
    dpg.show_item(object.capture.ID_sock_server_l2_port_visibility)
    #dpg.show_item("edge_2_sock_port_visible")
    dpg.show_item(object.slam.ID_sock_server_port_visibility)
    dpg.show_item(object.edge_1.ID_sock_server_l1_o)

    # Socket
    dpg.show_item(object.capture.ID_sock_client_l2)
    dpg.show_item(object.capture.ID_device_visibility)
    dpg.show_item(object.edge_1.ID_sock_client_l2_o)
    dpg.show_item(object.control.ID_sock_server_l2)
    dpg.show_item(object.edge_1.ID_sock_server_l2_i)
    dpg.show_item(object.capture.ID_sock_server_l2)
    dpg.show_item(object.edge_1.ID_sock_client_l1_i)
    dpg.show_item(object.edge_1.ID_sock_client_l1_o)

def set_mode_demo():
    # Block
    dpg.show_item("node_block_train")
    dpg.show_item("node_block_edge")
    dpg.show_item("node_block_cloud")

    # Icon
    dpg.show_item(object.train.ID_icon_lidar_visibility)
    dpg.show_item("icon_computer_visible")

    # Misc
    dpg.hide_item(object.control.ID_temperature_visibility)
    dpg.hide_item(object.operator.ID_mqtt_broker_port_visibility)
    dpg.hide_item(object.edge_1.ID_mqtt_visibility)
    dpg.hide_item(object.operator.ID_mqtt_topic_visibility)
    #dpg.hide_item(object.edge_1.ID_ip_visibility)
    dpg.hide_item(object.train.ID_geoloc_status)
    dpg.hide_item("l2_plot_visible")

    # Mongo
    dpg.hide_item("table_mongo")

    # IP
    #dpg.hide_item(object.edge_1.ID_ip_visibility)
    dpg.hide_item(object.capture.ID_ip_visibility)
    dpg.hide_item(object.operator.ID_ip_visibility)

    # LiDARs
    dpg.hide_item(object.train.ID_l1_line_visibility)
    dpg.hide_item(object.train.ID_l1_ip_visibility)
    dpg.hide_item(object.train.ID_l1_motor_speed_visibility)
    dpg.hide_item(object.train.ID_l1_sock_client_port_visibility)
    dpg.hide_item(object.edge_1.ID_source_1)
    dpg.hide_item(object.edge_1.ID_source_2)
    dpg.hide_item(object.edge_1.ID_sock_client_l1_i)
    dpg.hide_item(object.edge_1.ID_sock_client_l1_o)

    dpg.hide_item(object.train.ID_l2_line_visibility)
    dpg.hide_item(object.train.ID_l2_ip_visibility)
    dpg.hide_item(object.train.ID_l2_motor_speed_visibility)
    dpg.hide_item(object.train.ID_l2_sock_client_port_visibility)
    dpg.show_item(object.edge_1.ID_sock_client_l2_o)
    dpg.hide_item(object.edge_1.ID_sock_client_l2_o)
    dpg.hide_item(object.edge_1.ID_sock_client_l2_source)
    if(param_interface.lidar_main == "lidar_1"):
        dpg.show_item(object.train.ID_l1_status)
        dpg.show_item(object.train.ID_l1_motor_visibility)
        dpg.show_item(object.train.ID_l1_stat_visibility)
        dpg.show_item("link_l1_py")
        dpg.show_item(object.capture.ID_sock_server_l1)
        dpg.show_item(object.capture.ID_sock_client_l1)
        dpg.show_item(object.edge_1.ID_sock_server_l1_i)
        dpg.show_item("link_capture_edge_l1_sock")
        dpg.show_item(object.edge_1.ID_sock_client_l1_i)
        dpg.show_item(object.edge_1.ID_sock_client_l1_o)

        dpg.hide_item(object.train.ID_l2_status)
        dpg.hide_item(object.train.ID_l2_motor_visibility)
        dpg.hide_item(object.train.ID_l2_stat_visibility)
        dpg.hide_item("link_l2_py")
        dpg.hide_item(object.capture.ID_sock_server_l2)
        dpg.hide_item(object.capture.ID_sock_client_l2)
        dpg.hide_item(object.edge_1.ID_sock_server_l2_i)
        dpg.hide_item(object.edge_1.ID_sock_client_l2_o)
        dpg.hide_item("link_capture_edge_l2_sock")
    if(param_interface.lidar_main == "lidar_2"):
        dpg.show_item(object.train.ID_l2_status)
        dpg.show_item(object.train.ID_l2_motor_visibility)
        dpg.show_item(object.train.ID_l2_stat_visibility)
        dpg.show_item("link_l2_py")
        dpg.show_item(object.capture.ID_sock_server_l2)
        dpg.show_item(object.capture.ID_sock_client_l2)
        dpg.show_item(object.edge_1.ID_sock_server_l2_i)
        dpg.show_item(object.edge_1.ID_sock_client_l2_o)
        dpg.show_item("link_capture_edge_l2_sock")

        dpg.hide_item(object.train.ID_l1_status)
        dpg.hide_item(object.train.ID_l1_motor_visibility)
        dpg.hide_item(object.train.ID_l1_stat_visibility)
        dpg.hide_item("link_l1_py")
        dpg.hide_item(object.capture.ID_sock_server_l1)
        dpg.hide_item(object.capture.ID_sock_client_l1)
        dpg.hide_item(object.edge_1.ID_sock_server_l1_i)
        dpg.hide_item("link_capture_edge_l1_sock")
        dpg.hide_item(object.edge_1.ID_sock_client_l1_i)
        dpg.hide_item(object.edge_1.ID_sock_client_l1_o)

    # Nodes
    dpg.hide_item("node_slam")
    dpg.hide_item("node_ai")
    dpg.hide_item("node_edge_2")
    dpg.hide_item("node_ssd")
    dpg.hide_item("node_cloud_car")
    dpg.hide_item("node_control")

    dpg.show_item("node_capture")
    dpg.show_item("node_edge_1")
    dpg.show_item("node_edge_2")
    dpg.show_item("node_data")
    dpg.show_item("node_operator")
    dpg.show_item("node_train")

    dpg.configure_viewport("viewport", title="System control interface")

    # Links
    dpg.hide_item("link_va_hu")
    dpg.hide_item("link_ai_edge_1_http")
    #dpg.hide_item("link_edge_2_edge_1_http")
    #dpg.hide_item("link_edge_2_edge_sock")
    #dpg.hide_item("link_edge_edge_2_sock")
    #dpg.hide_item("link_edge_edge_2_http")
    dpg.hide_item("link_edge_interface_l1_sock")
    dpg.hide_item("link_edge_interface_l2_sock")
    dpg.hide_item("link_edge_processing_http")
    dpg.hide_item("link_edge_processing_sock")
    #dpg.hide_item("link_edge_2_edge_sock")
    #dpg.hide_item("link_edge_2_edge_1_http")
    dpg.hide_item("link_capture_geo")
    dpg.hide_item("link_interface_edge_1_http")
    dpg.hide_item("link_interface_ssd")

    # Nb threads
    dpg.hide_item(object.edge_1.ID_thread_visibility)
    dpg.hide_item(object.capture.ID_thread_visibility)

    # HTTP ports
    dpg.hide_item(object.capture.ID_http_server_port_visibility)
    dpg.hide_item(object.edge_1.ID_http_server_port_visibility)
    #dpg.hide_item("edge_2_http_port_visible")
    dpg.hide_item(object.edge_1.ID_http_server_o)
    dpg.hide_item(object.edge_1.ID_http_client_o)

    # Socket ports
    dpg.hide_item(object.control.ID_sock_server_l1_port_visibility)
    dpg.hide_item(object.control.ID_sock_server_l2_port_visibility)
    dpg.hide_item(object.edge_1.ID_sock_server_l1_port_visibility)
    dpg.hide_item(object.edge_1.ID_sock_server_l2_port_visibility)
    dpg.hide_item(object.capture.ID_sock_server_l1_port_visibility)
    dpg.hide_item(object.capture.ID_sock_server_l2_port_visibility)
    #dpg.hide_item("edge_2_sock_port_visible")
    dpg.hide_item(object.slam.ID_sock_server_port_visibility)
    dpg.hide_item(object.edge_1.ID_sock_server_l1_o)

    # Socket
    dpg.hide_item(object.capture.ID_device_visibility)

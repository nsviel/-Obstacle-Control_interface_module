#---------------------------------------------
from src.param import param_interface
from src.connection.HTTPS import https_client_get
from src.connection.HTTPS import https_client_post
from src.connection.SOCK import sock_server
from src.scheme.loop import scheme_update
from src.scheme.loop import scheme_mode

import dearpygui.dearpygui as dpg


def set_mode():
    if(param_interface.status_ui == "param"):
        set_mode_dev()
        scheme_mode.update_node_pos_dev()
    elif(param_interface.status_ui == "overview"):
        set_mode_demo()
        scheme_mode.update_node_pos_demo_minimized()
    elif(param_interface.status_ui == "overview_fullscreen"):
        set_mode_demo()
        scheme_mode.update_node_pos_demo_fullscreen()

def set_mode_dev():
    # Block
    dpg.hide_item("node_block_train")
    dpg.hide_item("node_block_edge")
    dpg.hide_item("node_block_cloud")

    # Icon
    dpg.hide_item("icon_lidar_visible")
    dpg.hide_item("icon_computer_visible")

    # Misc
    dpg.show_item("interface_temp_visibile")
    dpg.show_item("ai_trainope_port_visible")
    dpg.show_item("edge_mqtt_visible")
    dpg.show_item("trainope_mqtt_topic_visible")
    dpg.show_item("edge_edge_id_visible")
    dpg.show_item("geo_status")
    dpg.show_item("l2_plot_visible")

    # IP
    dpg.show_item("edge_ip_visible")
    dpg.show_item("capture_ip_visible")
    dpg.show_item("ip_operator_visible")

    # Mongo
    dpg.show_item("table_mongo")

    # LiDARs
    dpg.show_item("l1_status")
    dpg.show_item("l1_motor_visible")
    dpg.show_item("l1_perf_visible")
    dpg.show_item("link_l1_py")
    dpg.show_item("capture_l1_in")
    dpg.show_item("capture_l1_out")
    dpg.show_item("edge_sock_client_l1_o")
    dpg.show_item("edge_sock_server_l1_i")
    dpg.show_item("link_capture_edge_l1_sock")
    dpg.show_item("edge_sock_client_l1_i")
    dpg.show_item("l1_line_visible")
    dpg.show_item("l1_params_visible")
    dpg.show_item("l1_speedgenext_visible")
    dpg.show_item("l1_port_visible")
    dpg.show_item("edge_src_1")
    dpg.show_item("edge_src_2")
    dpg.show_item("l2_line_visible")
    dpg.show_item("l2_params_visible")
    dpg.show_item("l2_speedgenext_visible")
    dpg.show_item("edge_sock_client_l2_source")
    dpg.show_item("l2_port_visible")
    dpg.show_item("edge_sock_client_l2_o")
    dpg.show_item("l2_status")
    dpg.show_item("l2_motor_visible")
    dpg.show_item("l2_perf_visible")
    dpg.show_item("link_l2_py")
    dpg.show_item("capture_l2_in")
    dpg.show_item("capture_l2_out")
    dpg.show_item("edge_sock_server_l2_i")
    dpg.show_item("link_capture_edge_l2_sock")

    # SSD
    dpg.show_item("ssd_param_visible")
    dpg.show_item("ssd_l1_visible")
    dpg.show_item("ssd_l2_visible")

    # Nodes
    dpg.show_item("node_ve")
    dpg.show_item("node_ai")
    dpg.show_item("node_ed")
    dpg.show_item("node_ssd")
    dpg.show_item("node_cloud_car")
    dpg.show_item("node_co")
    dpg.configure_viewport("viewport", title="module_interface")

    # Links
    dpg.show_item("link_l2_py")
    dpg.show_item("link_va_hu")
    dpg.show_item("link_ai_edge_http")
    dpg.show_item("link_edgenext_edge_http")
    dpg.show_item("link_edgenext_edge_sock")
    dpg.show_item("link_edge_edgenext_sock")
    dpg.show_item("link_edge_edgenext_http")
    dpg.show_item("link_edge_interface_l1_sock")
    dpg.show_item("link_edge_interface_l2_sock")
    dpg.show_item("link_edge_processing_http")
    dpg.show_item("link_edge_processing_sock")

    dpg.show_item("link_edgenext_edge_sock")
    dpg.show_item("link_edgenext_edge_http")
    dpg.show_item("link_capture_geo")
    dpg.show_item("link_capture_edge_l2_sock")
    dpg.show_item("link_interface_edge_http")
    dpg.show_item("link_interface_ssd")

    # Nb threads
    dpg.show_item("interface_thread_visible")
    dpg.show_item("edge_thread_visible")
    dpg.show_item("capture_thread_visible")

    # HTTP ports
    dpg.show_item("capture_http_port_visible")
    dpg.show_item("edge_http_port_visible")
    dpg.show_item("edgenext_http_port_visible")
    dpg.show_item("edge_http_server_o")
    dpg.show_item("edge_http_client_o")

    # Socket ports
    dpg.show_item("interface_port_l1_visible")
    dpg.show_item("interface_port_l2_visible")
    dpg.show_item("edge_port_l1_visible")
    dpg.show_item("edge_port_l2_visible")
    dpg.show_item("capture_l1_port_visible")
    dpg.show_item("capture_l2_port_visible")
    dpg.show_item("edgenext_sock_port_visible")
    dpg.show_item("processing_sock_port_visible")
    dpg.show_item("edge_sock_server_l1_o")

    # Socket
    dpg.show_item("capture_l2_out")
    dpg.show_item("capture_lidar_dev_visible")
    dpg.show_item("edge_sock_client_l2_o")
    dpg.show_item("interface_sock_server_l2")
    dpg.show_item("edge_sock_server_l2_i")
    dpg.show_item("capture_l2_in")
    dpg.show_item("edge_sock_client_l1_i")
    dpg.show_item("edge_sock_client_l1_o")

def set_mode_demo():
    # Block
    dpg.show_item("node_block_train")
    dpg.show_item("node_block_edge")
    dpg.show_item("node_block_cloud")

    # Icon
    dpg.show_item("icon_lidar_visible")
    dpg.show_item("icon_computer_visible")

    # Misc
    dpg.hide_item("interface_temp_visibile")
    dpg.hide_item("ai_trainope_port_visible")
    dpg.hide_item("edge_mqtt_visible")
    dpg.hide_item("trainope_mqtt_topic_visible")
    dpg.hide_item("edge_edge_id_visible")
    dpg.hide_item("geo_status")
    dpg.hide_item("l2_plot_visible")

    # Mongo
    dpg.hide_item("table_mongo")

    # IP
    dpg.hide_item("edge_ip_visible")
    dpg.hide_item("capture_ip_visible")
    dpg.hide_item("ip_operator_visible")

    # LiDARs
    dpg.hide_item("l1_line_visible")
    dpg.hide_item("l1_params_visible")
    dpg.hide_item("l1_speedgenext_visible")
    dpg.hide_item("l1_port_visible")
    dpg.hide_item("edge_src_1")
    dpg.hide_item("edge_src_2")
    dpg.hide_item("edge_sock_client_l1_i")
    dpg.hide_item("edge_sock_client_l1_o")

    dpg.hide_item("l2_line_visible")
    dpg.hide_item("l2_params_visible")
    dpg.hide_item("l2_speedgenext_visible")
    dpg.hide_item("l2_port_visible")
    dpg.show_item("edge_sock_client_l2_o")
    dpg.hide_item("edge_sock_client_l2_o")
    dpg.hide_item("edge_sock_client_l2_source")
    if(param_interface.lidar_main == "lidar_1"):
        dpg.show_item("l1_status")
        dpg.show_item("l1_motor_visible")
        dpg.show_item("l1_perf_visible")
        dpg.show_item("link_l1_py")
        dpg.show_item("capture_l1_in")
        dpg.show_item("capture_l1_out")
        dpg.show_item("edge_sock_server_l1_i")
        dpg.show_item("link_capture_edge_l1_sock")
        dpg.show_item("edge_sock_client_l1_i")
        dpg.show_item("edge_sock_client_l1_o")

        dpg.hide_item("l2_status")
        dpg.hide_item("l2_motor_visible")
        dpg.hide_item("l2_perf_visible")
        dpg.hide_item("link_l2_py")
        dpg.hide_item("capture_l2_in")
        dpg.hide_item("capture_l2_out")
        dpg.hide_item("edge_sock_server_l2_i")
        dpg.hide_item("edge_sock_client_l2_o")
        dpg.hide_item("link_capture_edge_l2_sock")
    if(param_interface.lidar_main == "lidar_2"):
        dpg.show_item("l2_status")
        dpg.show_item("l2_motor_visible")
        dpg.show_item("l2_perf_visible")
        dpg.show_item("link_l2_py")
        dpg.show_item("capture_l2_in")
        dpg.show_item("capture_l2_out")
        dpg.show_item("edge_sock_server_l2_i")
        dpg.show_item("edge_sock_client_l2_o")
        dpg.show_item("link_capture_edge_l2_sock")

        dpg.hide_item("l1_status")
        dpg.hide_item("l1_motor_visible")
        dpg.hide_item("l1_perf_visible")
        dpg.hide_item("link_l1_py")
        dpg.hide_item("capture_l1_in")
        dpg.hide_item("capture_l1_out")
        dpg.hide_item("edge_sock_server_l1_i")
        dpg.hide_item("link_capture_edge_l1_sock")
        dpg.hide_item("edge_sock_client_l1_i")
        dpg.hide_item("edge_sock_client_l1_o")

    # Nodes
    dpg.hide_item("node_ve")
    dpg.hide_item("node_ai")
    dpg.hide_item("node_ed")
    dpg.hide_item("node_ssd")
    dpg.hide_item("node_cloud_car")
    dpg.hide_item("node_co")

    dpg.show_item("node_py")
    dpg.show_item("node_hu")
    dpg.show_item("node_data")
    dpg.show_item("node_operator")
    dpg.show_item("node_train")

    dpg.configure_viewport("viewport", title="System control interface")

    # Links
    dpg.hide_item("link_va_hu")
    dpg.hide_item("link_ai_edge_http")
    dpg.hide_item("link_edgenext_edge_http")
    dpg.hide_item("link_edgenext_edge_sock")
    dpg.hide_item("link_edge_edgenext_sock")
    dpg.hide_item("link_edge_edgenext_http")
    dpg.hide_item("link_edge_interface_l1_sock")
    dpg.hide_item("link_edge_interface_l2_sock")
    dpg.hide_item("link_edge_processing_http")
    dpg.hide_item("link_edge_processing_sock")
    dpg.hide_item("link_edgenext_edge_sock")
    dpg.hide_item("link_edgenext_edge_http")
    dpg.hide_item("link_capture_geo")
    dpg.hide_item("link_interface_edge_http")
    dpg.hide_item("link_interface_ssd")

    # Nb threads
    dpg.hide_item("edge_thread_visible")
    dpg.hide_item("capture_thread_visible")

    # HTTP ports
    dpg.hide_item("capture_http_port_visible")
    dpg.hide_item("edge_http_port_visible")
    dpg.hide_item("edgenext_http_port_visible")
    dpg.hide_item("edge_http_server_o")
    dpg.hide_item("edge_http_client_o")

    # Socket ports
    dpg.hide_item("interface_port_l1_visible")
    dpg.hide_item("interface_port_l2_visible")
    dpg.hide_item("edge_port_l1_visible")
    dpg.hide_item("edge_port_l2_visible")
    dpg.hide_item("capture_l1_port_visible")
    dpg.hide_item("capture_l2_port_visible")
    dpg.hide_item("edgenext_sock_port_visible")
    dpg.hide_item("processing_sock_port_visible")
    dpg.hide_item("edge_sock_server_l1_o")

    # Socket
    dpg.hide_item("capture_lidar_dev_visible")

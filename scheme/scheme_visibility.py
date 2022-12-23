#---------------------------------------------
from param import param_co
from HTTPS import https_client_get
from HTTPS import https_client_post
from SOCK import sock_server
from scheme import scheme_update

import dearpygui.dearpygui as dpg


def set_mode():
    if(param_co.status_ui == "dev"):
        set_mode_dev()
        scheme_update.update_node_pos_dev()
    elif(param_co.status_ui == "demo_minimized"):
        set_mode_demo()
        scheme_update.update_node_pos_demo_minimized()
    elif(param_co.status_ui == "demo_fullscreen"):
        set_mode_demo()
        scheme_update.update_node_pos_demo_fullscreen()

def set_mode_dev():
    # Block
    dpg.hide_item("node_block_train")
    dpg.hide_item("node_block_edge")
    dpg.hide_item("node_block_cloud")

    # Icon
    dpg.hide_item("icon_lidar_visible")
    dpg.hide_item("icon_computer_visible")

    # Misc
    dpg.show_item("co_temp_visibile")
    dpg.show_item("ai_sncf_port_visible")
    dpg.show_item("hu_mqtt_visible")
    dpg.show_item("sncf_mqtt_topic_visible")
    dpg.show_item("hu_edge_id_visible")
    dpg.show_item("geo_status")
    dpg.show_item("l2_plot_visible")

    # IP
    dpg.show_item("hu_ip_visible")
    dpg.show_item("py_ip_visible")
    dpg.show_item("sncf_ip_visible")

    # LiDARs
    dpg.show_item("l1_status")
    dpg.show_item("l1_motor_visible")
    dpg.show_item("l1_perf_visible")
    dpg.show_item("link_l1_py")
    dpg.show_item("py_l1_in")
    dpg.show_item("py_l1_out")
    dpg.show_item("hu_sock_client_l1_o")
    dpg.show_item("hu_sock_server_l1_i")
    dpg.show_item("link_py_hu_l1_sock")
    dpg.show_item("hu_sock_client_l1_i")
    dpg.show_item("l1_line_visible")
    dpg.show_item("l1_params_visible")
    dpg.show_item("l1_speed_visible")
    dpg.show_item("l1_port_visible")
    dpg.show_item("hu_src_1")
    dpg.show_item("hu_src_2")
    dpg.show_item("l2_line_visible")
    dpg.show_item("l2_params_visible")
    dpg.show_item("l2_speed_visible")
    dpg.show_item("l2_port_visible")
    dpg.show_item("hu_sock_client_l2_o")
    dpg.show_item("hu_sock_client_l2_o")
    dpg.show_item("combo_lidar")

    # SSD
    dpg.show_item("ssd_param_visible")
    dpg.show_item("ssd_l1_visible")
    dpg.show_item("ssd_l2_visible")

    # Nodes
    dpg.show_item("node_ve")
    dpg.show_item("node_ai")
    dpg.show_item("node_ed")
    dpg.show_item("node_ssd")
    dpg.show_item("node_valeo")
    dpg.show_item("node_co")
    dpg.configure_viewport("viewport", title="Controlium")

    # Links
    dpg.show_item("link_l2_py")
    dpg.show_item("link_va_hu")
    dpg.show_item("link_ai_hu_http")

    dpg.show_item("link_ed_hu_http")
    dpg.show_item("link_ed_hu_sock")

    dpg.show_item("link_hu_ed_sock")
    dpg.show_item("link_hu_ed_http")
    dpg.show_item("link_hu_co_l1_sock")
    dpg.show_item("link_hu_co_l2_sock")
    dpg.show_item("link_hu_ve_http")
    dpg.show_item("link_hu_ve_sock")

    dpg.show_item("link_ed_hu_sock")
    dpg.show_item("link_ed_hu_http")

    dpg.show_item("link_py_geo")
    dpg.show_item("link_py_hu_l2_sock")

    dpg.show_item("link_co_hu_http")
    dpg.show_item("link_co_ssd")

    # Nb threads
    dpg.show_item("co_thread_visible")
    dpg.show_item("hu_thread_visible")
    dpg.show_item("py_thread_visible")

    # HTTP ports
    dpg.show_item("py_http_port_visible")
    dpg.show_item("hu_http_port_visible")
    dpg.show_item("ed_http_port_visible")
    dpg.show_item("hu_http_server_o")
    dpg.show_item("hu_http_client_o")

    # Socket ports
    dpg.show_item("co_port_l1_visible")
    dpg.show_item("co_port_l2_visible")
    dpg.show_item("hu_port_l1_visible")
    dpg.show_item("hu_port_l2_visible")
    dpg.show_item("py_l1_port_visible")
    dpg.show_item("py_l2_port_visible")
    dpg.show_item("ed_sock_port_visible")
    dpg.show_item("ve_sock_port_visible")
    dpg.show_item("hu_sock_server_l1_o")

    # Socket
    dpg.show_item("py_l2_out")
    dpg.show_item("py_lidar_dev_visible")
    dpg.show_item("hu_sock_client_l2_o")
    dpg.show_item("co_sock_server_l2")
    dpg.show_item("hu_sock_server_l2_i")
    dpg.show_item("py_l2_in")
    dpg.show_item("hu_sock_client_l1_i")
    dpg.show_item("hu_sock_client_l1_o")

def set_mode_demo():
    # Block
    dpg.show_item("node_block_train")
    dpg.show_item("node_block_edge")
    dpg.show_item("node_block_cloud")

    # Icon
    dpg.show_item("icon_lidar_visible")
    dpg.show_item("icon_computer_visible")

    # Misc
    dpg.hide_item("co_temp_visibile")
    dpg.hide_item("ai_sncf_port_visible")
    dpg.hide_item("hu_mqtt_visible")
    dpg.hide_item("sncf_mqtt_topic_visible")
    dpg.hide_item("hu_edge_id_visible")
    dpg.hide_item("geo_status")
    dpg.hide_item("l2_plot_visible")

    # IP
    dpg.hide_item("hu_ip_visible")
    dpg.hide_item("py_ip_visible")
    dpg.hide_item("sncf_ip_visible")

    # LiDARs
    dpg.hide_item("l1_line_visible")
    dpg.hide_item("l1_params_visible")
    dpg.hide_item("l1_speed_visible")
    dpg.hide_item("l1_port_visible")
    dpg.hide_item("hu_src_1")
    dpg.hide_item("hu_src_2")
    dpg.hide_item("combo_lidar")
    dpg.hide_item("hu_sock_client_l1_i")
    dpg.hide_item("hu_sock_client_l1_o")

    dpg.hide_item("l2_line_visible")
    dpg.hide_item("l2_params_visible")
    dpg.hide_item("l2_speed_visible")
    dpg.hide_item("l2_port_visible")
    dpg.show_item("hu_sock_client_l2_o")
    dpg.hide_item("hu_sock_client_l2_o")
    dpg.hide_item("hu_sock_client_l2_source")
    if(param_co.lidar_main == "lidar_1"):
        dpg.show_item("l1_status")
        dpg.show_item("l1_motor_visible")
        dpg.show_item("l1_perf_visible")
        dpg.show_item("link_l1_py")
        dpg.show_item("py_l1_in")
        dpg.show_item("py_l1_out")
        dpg.show_item("hu_sock_server_l1_i")
        dpg.show_item("link_py_hu_l1_sock")

        dpg.hide_item("l2_status")
        dpg.hide_item("l2_motor_visible")
        dpg.hide_item("l2_perf_visible")
        dpg.hide_item("link_l2_py")
        dpg.hide_item("py_l2_in")
        dpg.hide_item("py_l2_out")
        dpg.hide_item("hu_sock_server_l2_i")
        dpg.hide_item("hu_sock_client_l2_o")
        dpg.hide_item("link_py_hu_l2_sock")
    if(param_co.lidar_main == "lidar_2"):
        dpg.show_item("l2_status")
        dpg.show_item("l2_motor_visible")
        dpg.show_item("l2_perf_visible")
        dpg.show_item("link_l2_py")
        dpg.show_item("py_l2_in")
        dpg.show_item("py_l2_out")
        dpg.show_item("hu_sock_server_l2_i")
        dpg.show_item("link_py_hu_l2_sock")

        dpg.hide_item("l1_status")
        dpg.hide_item("l1_motor_visible")
        dpg.hide_item("l1_perf_visible")
        dpg.hide_item("link_l1_py")
        dpg.hide_item("py_l1_in")
        dpg.hide_item("py_l1_out")
        dpg.hide_item("hu_sock_server_l1_i")
        dpg.hide_item("link_py_hu_l1_sock")
        dpg.hide_item("hu_sock_client_l1_i")
        dpg.hide_item("hu_sock_client_l1_o")

    # Nodes
    dpg.hide_item("node_ve")
    dpg.hide_item("node_ai")
    dpg.hide_item("node_ed")
    dpg.hide_item("node_ssd")
    dpg.hide_item("node_valeo")
    dpg.hide_item("node_co")

    dpg.show_item("node_py")
    dpg.show_item("node_hu")
    dpg.show_item("node_data")
    dpg.show_item("node_sncf")
    dpg.show_item("node_train")

    dpg.configure_viewport("viewport", title="System control interface")

    # Links
    dpg.hide_item("link_va_hu")
    dpg.hide_item("link_ai_hu_http")
    dpg.hide_item("link_ed_hu_http")
    dpg.hide_item("link_ed_hu_sock")
    dpg.hide_item("link_hu_ed_sock")
    dpg.hide_item("link_hu_ed_http")
    dpg.hide_item("link_hu_co_l1_sock")
    dpg.hide_item("link_hu_co_l2_sock")
    dpg.hide_item("link_hu_ve_http")
    dpg.hide_item("link_hu_ve_sock")
    dpg.hide_item("link_ed_hu_sock")
    dpg.hide_item("link_ed_hu_http")
    dpg.hide_item("link_py_geo")
    dpg.hide_item("link_co_hu_http")
    dpg.hide_item("link_co_ssd")

    # Nb threads
    dpg.hide_item("hu_thread_visible")
    dpg.hide_item("py_thread_visible")

    # HTTP ports
    dpg.hide_item("py_http_port_visible")
    dpg.hide_item("hu_http_port_visible")
    dpg.hide_item("ed_http_port_visible")
    dpg.hide_item("hu_http_server_o")
    dpg.hide_item("hu_http_client_o")

    # Socket ports
    dpg.hide_item("co_port_l1_visible")
    dpg.hide_item("co_port_l2_visible")
    dpg.hide_item("hu_port_l1_visible")
    dpg.hide_item("hu_port_l2_visible")
    dpg.hide_item("py_l1_port_visible")
    dpg.hide_item("py_l2_port_visible")
    dpg.hide_item("ed_sock_port_visible")
    dpg.hide_item("ve_sock_port_visible")
    dpg.hide_item("hu_sock_server_l1_o")

    # Socket
    dpg.hide_item("py_lidar_dev_visible")

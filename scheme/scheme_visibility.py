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
    # Misc
    dpg.show_item("co_temp_visibile")
    dpg.show_item("ai_sncf_port_visible")
    dpg.show_item("hu_mqtt_visible")
    dpg.show_item("sncf_mqtt_topic_visible")
    dpg.show_item("hu_edge_id_visible")
    dpg.show_item("geo_status")
    dpg.show_item("l2_plot_visible")

    # LiDARs
    dpg.show_item("l1_line_visible")
    dpg.show_item("l2_line_visible")
    dpg.show_item("l1_params_visible")
    dpg.show_item("l2_params_visible")
    dpg.show_item("l2_status")
    dpg.show_item("l2_motor_visible")
    dpg.show_item("l2_perf_visible")
    dpg.show_item("l2_speed_visible")

    # SSD
    dpg.show_item("ssd_param_visible")
    dpg.show_item("ssd_l1_visible")
    dpg.show_item("ssd_l2_visible")

    # Nodes
    dpg.show_item("node_ed")
    dpg.show_item("node_valeo")
    dpg.hide_item("node_legend")
    dpg.configure_viewport("viewport", title="Controlium")
    dpg.set_item_label("node_co", "Controlium")
    dpg.set_item_label("node_hu", "Hubium")
    dpg.set_item_label("node_py", "Pywardium")
    dpg.set_item_label("node_train", "Train")
    dpg.set_item_label("node_ve", "Velodium")
    dpg.set_item_label("node_network", "Network")

    # Links
    dpg.show_item("link_l2_py")
    dpg.show_item("link_va_hu")
    dpg.show_item("link_hu_ed_sock")
    dpg.show_item("link_ed_hu_sock")
    dpg.show_item("link_hu_ed_http")
    dpg.show_item("link_ed_hu_http")
    dpg.show_item("link_py_geo")
    dpg.show_item("link_py_hu_l2_sock")
    dpg.show_item("link_hu_co_l2_sock")

    # Nb threads
    dpg.show_item("co_thread_visible")
    dpg.show_item("hu_thread_visible")
    dpg.show_item("py_thread_visible")

    # HTTP ports
    dpg.show_item("py_http_port_visible")
    dpg.show_item("hu_http_port_visible")
    dpg.show_item("ed_http_port_visible")
    dpg.show_item("ve_http_port_visible")
    dpg.show_item("ai_http_port_visible")

    # Socket ports
    dpg.show_item("co_port_l1_visible")
    dpg.show_item("co_port_l2_visible")
    dpg.show_item("hu_port_l1_visible")
    dpg.show_item("hu_port_l2_visible")
    dpg.show_item("py_l1_port_visible")
    dpg.show_item("py_l2_port_visible")
    dpg.show_item("ed_sock_port_visible")
    dpg.show_item("ve_sock_port_visible")

    # Socket
    dpg.show_item("py_l2_out")
    dpg.show_item("py_l2_dev_visible")
    dpg.show_item("hu_sock_client_l2_i")
    dpg.show_item("co_sock_server_l2")
    dpg.show_item("hu_sock_server_l2_i")
    dpg.show_item("py_l2_in")

def set_mode_demo():
    # Misc
    dpg.hide_item("co_temp_visibile")
    dpg.hide_item("ai_sncf_port_visible")
    dpg.hide_item("hu_mqtt_visible")
    dpg.hide_item("sncf_mqtt_topic_visible")
    dpg.hide_item("hu_edge_id_visible")
    dpg.hide_item("geo_status")
    dpg.hide_item("l2_plot_visible")

    # LiDARs
    dpg.hide_item("l1_line_visible")
    dpg.hide_item("l2_line_visible")
    dpg.hide_item("l1_params_visible")
    dpg.hide_item("l2_params_visible")
    dpg.hide_item("l2_status")
    dpg.hide_item("l2_motor_visible")
    dpg.hide_item("l2_perf_visible")
    dpg.hide_item("l2_speed_visible")

    # SSD
    dpg.hide_item("ssd_param_visible")
    dpg.hide_item("ssd_l1_visible")
    dpg.hide_item("ssd_l2_visible")

    # Nodes
    dpg.hide_item("node_ed")
    dpg.hide_item("node_valeo")
    dpg.show_item("node_legend")
    dpg.configure_viewport("viewport", title="System control interface")
    dpg.set_item_label("node_co", "System control interface")
    dpg.set_item_label("node_hu", "P2. Edge AI module")
    dpg.set_item_label("node_py", "P2. Train module")
    dpg.set_item_label("node_train", "LiDAR")
    dpg.set_item_label("node_ve", "Data processing")
    dpg.set_item_label("node_network", "KPI")

    # Links
    dpg.hide_item("link_l2_py")
    dpg.hide_item("link_va_hu")
    dpg.hide_item("link_hu_ed_sock")
    dpg.hide_item("link_ed_hu_sock")
    dpg.hide_item("link_hu_ed_http")
    dpg.hide_item("link_ed_hu_http")
    dpg.hide_item("link_py_geo")
    dpg.hide_item("link_py_hu_l2_sock")
    dpg.hide_item("link_hu_co_l2_sock")

    # Nb threads
    dpg.hide_item("co_thread_visible")
    dpg.hide_item("hu_thread_visible")
    dpg.hide_item("py_thread_visible")

    # HTTP ports
    dpg.hide_item("py_http_port_visible")
    dpg.hide_item("hu_http_port_visible")
    dpg.hide_item("ed_http_port_visible")
    dpg.hide_item("ve_http_port_visible")
    dpg.hide_item("ai_http_port_visible")

    # Socket ports
    dpg.hide_item("co_port_l1_visible")
    dpg.hide_item("co_port_l2_visible")
    dpg.hide_item("hu_port_l1_visible")
    dpg.hide_item("hu_port_l2_visible")
    dpg.hide_item("py_l1_port_visible")
    dpg.hide_item("py_l2_port_visible")
    dpg.hide_item("ed_sock_port_visible")
    dpg.hide_item("ve_sock_port_visible")

    # Socket
    dpg.hide_item("py_l2_out")
    dpg.hide_item("py_l2_dev_visible")
    dpg.hide_item("hu_sock_client_l2_i")
    dpg.hide_item("co_sock_server_l2")
    dpg.hide_item("hu_sock_server_l2_i")
    dpg.hide_item("py_l2_in")

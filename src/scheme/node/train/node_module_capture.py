#---------------------------------------------
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Data acquisition", tag="node_py"):
        scheme_function.add_image("icon_computer", "icon_computer_visible")

        scheme_function.add_status_i("capture_input", "capture_status_but", "capture_status")
        scheme_function.add_ip_wallet("capture_wallet", "capture_ip", "-", "capture_ip_visible")
        scheme_function.add_nb_thread("capture_thread", "capture_thread_visible")

        #scheme_function.add_iperf_py()

        scheme_function.add_port_fixe_i("capture_l1_in", "capture_l1_port", "capture_l1_port_visible")
        scheme_connection.add_sock_client_o_("capture_l1_out")
        scheme_function.add_port_fixe_i("capture_l2_in", "capture_l2_port", "capture_l2_port_visible")
        scheme_connection.add_sock_client_o_("capture_l2_out")

        scheme_function.add_lidar_device("capture_l1_device", "capture_l2_device", "capture_lidar_dev_visible")

        scheme_connection.add_http_server_o("capture_http_server")
        scheme_function.add_port_fixe("capture_http_server_port", "capture_http_port_visible")

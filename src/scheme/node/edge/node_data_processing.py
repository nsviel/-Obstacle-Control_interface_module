#---------------------------------------------
from src.scheme import scheme_function
from src.scheme import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Data processing", tag="node_ve"):
        scheme_function.add_status("processing_status_but", "processing_status")
        scheme_function.add_ip_wallet("processing_wallet", "processing_ip", "localhost", "processing_ip_visible")
        scheme_function.add_velo_option("processing_opt_slam", "processing_opt_view", "processing_opt_reset")
        scheme_connection.add_sock_server_o("processing_sock_server")
        scheme_function.add_port_fixe("processing_sock_server_port", "processing_sock_port_visible")
        scheme_connection.add_http_server_o("processing_http_server")
        scheme_function.add_port_fixe("processing_http_server_port", "processing_http_port_visible")

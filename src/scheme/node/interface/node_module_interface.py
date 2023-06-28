#---------------------------------------------
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="System control interface", tag="node_co"):
        scheme_function.add_status_o("interface_input", "interface_status_but", "interface_status")
        scheme_function.add_ip("interface_ip")
        scheme_function.add_nb_thread("interface_thread", "interface_thread_visible")
        scheme_function.add_temperature("interface_temp", "interface_temp_visibile")

        scheme_function.add_choice_edge("combo_edge")

        scheme_connection.add_http_client_i("interface_http_client")

        scheme_connection.add_sock_server_i("interface_sock_server_l1")
        scheme_function.add_port_co("interface_sock_server_l1_port", "interface_port_l1_visible")

        scheme_connection.add_sock_server_i("interface_sock_server_l2")
        scheme_function.add_port_co("interface_sock_server_l2_port", "interface_port_l2_visible")

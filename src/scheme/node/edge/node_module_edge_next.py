#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Edge - 2", tag="node_edge_2"):
        scheme_function.add_status("edgenext_status_but", "edgenext_status")
        scheme_function.add_ip_wallet("edgenext_wallet", "edgenext_ip", param_interface.state_edge["edge_next"]["add"], "edgenext_ip_visible")
        #scheme_function.add_edge_id("edgenext_edge_id")
        #scheme_function.add_country("edgenext_country")

        scheme_connection.add_sock_client_i("edgenext_sock_client")

        scheme_connection.add_sock_server_i("edgenext_sock_server")
        scheme_function.add_port_fixe("edgenext_sock_server_port", "edgenext_sock_port_visible")

        scheme_connection.add_http_client_i("edgenext_http_client")
        scheme_connection.add_http_server_i("edgenext_http_server")
        scheme_function.add_port_fixe("edgenext_http_server_port", "edgenext_http_port_visible")

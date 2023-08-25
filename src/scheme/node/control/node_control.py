#---------------------------------------------
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="System control interface", tag="node_control"):
        scheme_function.add_status_o("interface_input", object.object.control.ID_status_light, object.object.control.ID_status)
        scheme_function.add_ip(object.object.control.ID_ip)
        scheme_function.add_nb_thread(object.object.control.ID_thread, object.object.control.ID_thread_visibility)
        scheme_function.add_temperature(object.object.control.ID_temperature, object.object.control.ID_temperature_visibility)
        scheme_function.add_choice_edge(object.object.control.ID_setting_edge_selection)
        scheme_connection.add_http_client_i(object.object.control.ID_http_client)
        scheme_connection.add_sock_server_i(object.object.control.ID_sock_server_l1)
        scheme_function.add_port_co(object.object.control.ID_sock_server_l1_port, object.object.control.ID_sock_server_l1_port_visibility)
        scheme_connection.add_sock_server_i(object.object.control.ID_sock_server_l2)
        scheme_function.add_port_co(object.object.control.ID_sock_server_l2_port, object.object.control.ID_sock_server_l2_port_visibility)

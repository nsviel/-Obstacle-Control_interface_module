#---------------------------------------------
from src.param import param_interface
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def design_node(edge):
    with dpg.node(label="Edge", tag=edge.ID_node):
        # General info
        scheme_function.add_status(edge.ID_status_light, edge.ID_status)
        scheme_function.add_ip_wallet(edge.ID_wallet, edge.ID_ip, param_interface.state_control["edge_1"]["add"], edge.ID_ip_visibility)
        scheme_function.add_nb_thread(edge.ID_thread, edge.ID_thread_visibility)
        scheme_function.add_edge_id(edge.ID_edge_id, edge.ID_edge_id_visibility)
        scheme_function.add_country(edge.ID_edge_country)

        # MQTT
        scheme_function.add_mqtt(edge.ID_mqtt_client, edge.ID_mqtt_client_name, edge.ID_mqtt_visibility)
        scheme_function.add_false_alarm()

        # Socket
        scheme_connection.add_sock_server_i(edge.ID_sock_server_l1_i)
        scheme_function.add_port_hu(edge.ID_sock_server_l1_port, edge.ID_sock_server_l1_port_visibility)
        scheme_connection.add_sock_server_i(edge.ID_sock_server_l2_i)
        scheme_function.add_port_hu(edge.ID_sock_server_l2_port, edge.ID_sock_server_l2_port_visibility)
        scheme_connection.add_sock_client_source_io(edge.ID_sock_client_l1_i, edge.ID_sock_client_l1_o, edge.ID_sock_client_l1_lidar_main, edge.ID_source_1, edge.ID_source_2)
        scheme_connection.add_sock_client_source_o(edge.ID_sock_client_l2_o, edge.ID_sock_client_l2_source)

        # HTTP
        scheme_connection.add_http_client_io(edge.ID_http_client_i, edge.ID_http_client_o)
        scheme_connection.add_http_server_o(edge.ID_http_server_o)
        scheme_function.add_port_fixe(edge.ID_http_server_port, edge.ID_http_server_port_visibility)

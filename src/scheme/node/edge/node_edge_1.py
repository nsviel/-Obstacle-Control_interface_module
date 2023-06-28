#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Edge - 1", tag="node_edge_1"):
        # General info
        scheme_function.add_status("edge_1_status_marker", "edge_1_status")
        scheme_function.add_ip_wallet("edge_1_wallet", "edge_1_ip", param_interface.state_interface["edge"]["add"], "edge_1_ip_visible")
        scheme_function.add_nb_thread("edge_1_thread", "edge_1_thread_visible")
        scheme_function.add_edge_id("edge_1_ID", "edge_1_ID_visible")
        scheme_function.add_country("edge_1_country")

        # MQTT
        scheme_function.add_mqtt("edge_1_mqtt_client", "edge_1_mqtt_client_name", "edge_1_mqtt_visible")
        scheme_function.add_false_alarm()

        # Socket
        scheme_connection.add_sock_server_io("edge_1_sock_server_l1_i", "edge_1_sock_server_l1_o")
        scheme_function.add_port_hu("edge_1_sock_server_l1_port", "edge_1_port_l1_visible")
        scheme_connection.add_sock_server_i("edge_1_sock_server_l2_i")
        scheme_function.add_port_hu("edge_1_sock_server_l2_port", "edge_1_port_l2_visible")
        scheme_connection.add_sock_client_source_io("edge_1_sock_client_l1_i", "edge_1_sock_client_l1_o", "edge_1_sock_client_l1_combo_lidar_main", "edge_1_source_1", "edge_1_source_2")
        scheme_connection.add_sock_client_source_o("edge_1_sock_client_l2_o", "edge_1_sock_client_l2_source")

        # HTTP
        scheme_connection.add_http_client_io("edge_1_http_client_i", "edge_1_http_client_o")
        scheme_connection.add_http_server_o("edge_1_http_server_o")
        scheme_function.add_port_fixe("edge_1_http_server_port", "edge_1_http_port_visible")

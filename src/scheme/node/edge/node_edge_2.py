#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Edge - 2", tag="node_edge_2"):
        # General info
        scheme_function.add_status("edge_2_status_marker", "edge_2_status")
        scheme_function.add_ip_wallet("edge_2_wallet", "edge_2_ip", param_interface.state_edge_1["edge_next"]["add"], "edge_2_ip_visible")
        scheme_function.add_nb_thread("edge_2_thread", "edge_2_thread_visible")
        scheme_function.add_edge_id("edge_2_ID", "edge_2_ID_visible")
        scheme_function.add_country("edge_2_country")

        # MQTT
        scheme_function.add_mqtt("edge_2_mqtt_client", "edge_2_mqtt_client_name", "edge_2_mqtt_visible")
        scheme_function.add_false_alarm()

        # Socket
        #scheme_connection.add_sock_server_io("edge_2_sock_server_l1_i", "edge_2_sock_server_l1_o")
        #scheme_function.add_port_hu("edge_2_sock_server_l1_port", "edge_2_port_l1_visible")
        #scheme_connection.add_sock_server_i("edge_2_sock_server_l2_i")
        #scheme_function.add_port_hu("edge_2_sock_server_l2_port", "edge_2_port_l2_visible")
        #scheme_connection.add_sock_client_source_io("edge_2_sock_client_l1_i_l1_i", "edge_2_sock_client_l1_i_l1_o", "edge_2_sock_client_l1_i_l1_combo_lidar_main", "edge_2_source_1", "edge_2_source_2")
        #scheme_connection.add_sock_client_source_o("edge_2_sock_client_l1_i_l2_o", "edge_2_sock_client_l1_i_l2_source")

        # HTTP
        #scheme_connection.add_http_client_io("edge_2_http_client_i", "edge_2_http_client_o")
        #scheme_connection.add_http_server_o("edge_2_http_server_o")
        #scheme_function.add_port_fixe("edge_2_http_server_port", "edge_2_http_port_visible")

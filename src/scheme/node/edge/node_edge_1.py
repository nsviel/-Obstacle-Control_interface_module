#---------------------------------------------
from src.param import param_interface
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Edge", tag=object.object.edge_1.ID_node):
        # General info
        scheme_function.add_status(object.object.edge_1.ID_status_light, object.object.edge_1.ID_status)
        scheme_function.add_ip_wallet(object.object.edge_1.ID_wallet, object.object.edge_1.ID_ip, param_interface.state_control["edge_1"]["add"], object.object.edge_1.ID_ip_visibility)
        scheme_function.add_nb_thread(object.object.edge_1.ID_thread, object.object.edge_1.ID_thread_visibility)
        scheme_function.add_edge_id(object.object.edge_1.ID_edge_id, object.object.edge_1.ID_edge_id_visibility)
        scheme_function.add_country(object.object.edge_1.ID_edge_country)

        # MQTT
        scheme_function.add_mqtt(object.object.edge_1.ID_mqtt_client, object.object.edge_1.ID_mqtt_client_name, object.object.edge_1.ID_mqtt_visibility)
        scheme_function.add_false_alarm()

        # Socket
        scheme_connection.add_sock_server_i(object.object.edge_1.ID_sock_server_l1_i)
        scheme_function.add_port_hu(object.object.edge_1.ID_sock_server_l1_port, object.object.edge_1.ID_sock_server_l1_port_visibility)
        scheme_connection.add_sock_server_i(object.object.edge_1.ID_sock_server_l2_i)
        scheme_function.add_port_hu(object.object.edge_1.ID_sock_server_l2_port, object.object.edge_1.ID_sock_server_l2_port_visibility)
        scheme_connection.add_sock_client_source_io(object.object.edge_1.ID_sock_client_l1_i, object.object.edge_1.ID_sock_client_l1_o, object.object.edge_1.ID_sock_client_l1_lidar_main, object.object.edge_1.ID_source_1, object.object.edge_1.ID_source_2)
        scheme_connection.add_sock_client_source_o(object.object.edge_1.ID_sock_client_l2_o, object.object.edge_1.ID_sock_client_l2_source)

        # HTTP
        scheme_connection.add_http_client_io(object.object.edge_1.ID_http_client_i, object.object.edge_1.ID_http_client_o)
        scheme_connection.add_http_server_o(object.object.edge_1.ID_http_server_o)
        scheme_function.add_port_fixe(object.object.edge_1.ID_http_server_port, object.object.edge_1.ID_http_server_port_visibility)

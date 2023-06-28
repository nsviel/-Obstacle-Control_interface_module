#---------------------------------------------
from src.param import param_interface
from src.scheme import scheme_function
from src.scheme import scheme_connection

import dearpygui.dearpygui as dpg


def design_block():
    with dpg.node(label="Edge", tag="node_block_edge"):
        scheme_function.add_image("icon_server", "icon_server_visible")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.drawlist(tag="block_edge", width=350, height=550):
                pass

def design_node():
    with dpg.node(label="Edge orchestrator", tag="node_hu"):
        scheme_function.add_status("edge_status_but", "edge_status")
        scheme_function.add_ip_wallet("edge_wallet", "edge_ip", param_interface.state_interface["edge"]["add"], "edge_ip_visible")
        scheme_function.add_nb_thread("edge_thread", "edge_thread_visible")

        scheme_function.add_edge_id("edge_edge_id", "edge_edge_id_visible")
        scheme_function.add_country("edge_country")
        scheme_function.add_mqtt("edge_mqtt_client", "edge_mqtt_client_name", "edge_mqtt_visible")
        scheme_function.add_false_alarm()

        scheme_connection.add_sock_server_io("edge_sock_server_l1_i", "edge_sock_server_l1_o")
        scheme_function.add_port_hu("edge_sock_server_l1_port", "edge_port_l1_visible")
        scheme_connection.add_sock_server_i("edge_sock_server_l2_i")
        scheme_function.add_port_hu("edge_sock_server_l2_port", "edge_port_l2_visible")

        scheme_connection.add_sock_client_source_io("edge_sock_client_l1_i", "edge_sock_client_l1_o", "edge_sock_client_l1_combo_lidar_main", "edge_src_1", "edge_src_2")
        scheme_connection.add_sock_client_source_o("edge_sock_client_l2_o", "edge_sock_client_l2_source")

        scheme_connection.add_http_client_io("edge_http_client_i", "edge_http_client_o")
        scheme_connection.add_http_server_o("edge_http_server_o")
        scheme_function.add_port_fixe("edge_http_server_port", "edge_http_port_visible")

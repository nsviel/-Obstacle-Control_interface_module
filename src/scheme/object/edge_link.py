#---------------------------------------------
from src.utils import function


class Edge_link:
    # Internal links
    ID_link_ai_http = function.id_generator();
    ID_link_slam_http = function.id_generator();
    ID_link_slam_socket = function.id_generator();
    def create_link_internal(edge):
        dpg.add_node_link(edge.ID_http_client_i, edge.ai.ID_http_server, tag=ID_link_ai_http)
        dpg.add_node_link(edge.ID_http_client_i, edge.slam.ID_http_server, tag=ID_link_slam_http)
        dpg.add_node_link(edge.slam.ID_sock_server, edge.ID_sock_client_l1_i, tag=ID_link_slam_socket)

    # External links
    ID_link_control_http = function.id_generator();
    ID_link_control_l1_sock = function.id_generator();
    ID_link_control_l2_sock = function.id_generator();
    ID_link_control_ssd = function.id_generator();
    ID_link_operator_mqtt = function.id_generator();
    ID_link_train_l1_sock = function.id_generator();
    ID_link_train_l2_sock = function.id_generator();
    ID_link_train_http = function.id_generator();
    def create_link_external(edge):
        dpg.add_node_link(object.object.control.ID_http_client, edge.ID_http_server_o, tag=ID_link_control_http)
        dpg.add_node_link(object.object.control.ID_sock_server_l1, edge.ID_sock_client_l1_o, tag=ID_link_control_l1_sock)
        dpg.add_node_link(object.object.control.ID_sock_server_l2, edge.ID_sock_client_l2_o, tag=ID_link_control_l2_sock)
        dpg.add_node_link("interface_input", "ssd_input", tag=ID_link_control_ssd)
        dpg.add_node_link(edge.ID_mqtt_client, object.object.operator.ID_mqtt_broker, tag=ID_link_operator_mqtt)
        dpg.add_node_link(object.object.capture.ID_sock_client_l1, object.object.edge_1.ID_sock_server_l1_i, tag=ID_link_train_l1_sock)
        dpg.add_node_link(object.object.capture.ID_sock_client_l2, object.object.edge_1.ID_sock_server_l2_i, tag=ID_link_train_l2_sock)
        dpg.add_node_link(object.object.capture.ID_http_server, object.object.edge_1.ID_http_client_i, tag=ID_link_train_http)

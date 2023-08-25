#---------------------------------------------
from src.utils import function
from src.scheme.object import edge_link


class Edge:
    name = "Edge"
    link = edge_link.Edge_link()

    # Info
    ID_status = function.id_generator();
    ID_status_light = function.id_generator();
    ID_ip = function.id_generator();
    ID_ip_visibility = function.id_generator();
    ID_edge_id = function.id_generator();
    ID_edge_id_visibility = function.id_generator();
    ID_edge_country = function.id_generator();
    ID_wallet = function.id_generator();
    ID_thread = function.id_generator();
    ID_thread_visibility = function.id_generator();

    # HTTP
    ID_http_client_i = function.id_generator();
    ID_http_client_o = function.id_generator();
    ID_http_server_o = function.id_generator();
    ID_http_server_port = function.id_generator();
    ID_http_server_port_visibility = function.id_generator();

    # MQTT
    ID_mqtt_client = function.id_generator();
    ID_mqtt_client_name = function.id_generator();
    ID_mqtt_visibility = function.id_generator();

    # Socket
    ID_sock_server_l1_i = function.id_generator();
    ID_sock_server_l1_o = function.id_generator();
    ID_sock_server_l1_port = function.id_generator();
    ID_sock_server_l1_port_visibility = function.id_generator();
    ID_sock_client_l1_i = function.id_generator();
    ID_sock_client_l1_o = function.id_generator();
    ID_sock_client_l1_lidar_main = function.id_generator();

    ID_sock_server_l2_i = function.id_generator();
    ID_sock_server_l2_port = function.id_generator();
    ID_sock_server_l2_port_visibility = function.id_generator();
    ID_sock_client_l2_o = function.id_generator();
    ID_sock_client_l2_source = function.id_generator();

    ID_source_1 = function.id_generator();
    ID_source_2 = function.id_generator();

    # Setting
    ID_setting_lidar_height = function.id_generator();
    ID_setting_threshold = function.id_generator();

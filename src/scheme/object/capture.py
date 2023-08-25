#---------------------------------------------
from src.utils import function


class Capture:
    # Info
    ID_status = function.id_generator();
    ID_status_light = function.id_generator();
    ID_ip = function.id_generator();
    ID_ip_visibility = function.id_generator();
    ID_wallet = function.id_generator();
    ID_thread = function.id_generator();
    ID_thread_visibility = function.id_generator();

    # HTTP
    ID_http_server = function.id_generator();
    ID_http_server_port = function.id_generator();
    ID_http_server_port_visibility = function.id_generator();

    # Socket
    ID_sock_server_l1 = function.id_generator();
    ID_sock_server_l1_port = function.id_generator();
    ID_sock_server_l1_port_visibility = function.id_generator();
    ID_sock_client_l1 = function.id_generator();
    ID_sock_server_l2 = function.id_generator();
    ID_sock_server_l2_port = function.id_generator();
    ID_sock_server_l2_port_visibility = function.id_generator();
    ID_sock_client_l2 = function.id_generator();

    # Setting
    ID_device_l1 = function.id_generator();
    ID_device_l2 = function.id_generator();
    ID_device_visibility = function.id_generator();

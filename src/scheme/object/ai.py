#---------------------------------------------
from src.utils import function


class AI:
    # Info
    ID_status = function.id_generator();
    ID_status_light = function.id_generator();
    ID_ip = function.id_generator();
    ID_ip_visibility = function.id_generator();
    ID_wallet = function.id_generator();

    # HTTP
    ID_http_server = function.id_generator();
    ID_http_server_port = function.id_generator();
    ID_http_server_port_visibility = function.id_generator();

    # Setting
    ID_setting_lidar_height = function.id_generator();
    ID_setting_threshold = function.id_generator();

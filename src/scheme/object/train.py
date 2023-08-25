#---------------------------------------------
from src.utils import function


class Train:
    # Info
    ID_icon_lidar = function.id_generator();
    ID_icon_lidar_visibility = function.id_generator();
    ID_geoloc_status = function.id_generator();
    ID_geoloc_country = function.id_generator();

    # LiDAR 1
    ID_l1_line_visibility = function.id_generator();
    ID_l1_status = function.id_generator();
    ID_l1_status_light = function.id_generator();
    ID_l1_activated = function.id_generator();
    ID_l1_ip = function.id_generator();
    ID_l1_ip_visibility = function.id_generator();
    ID_l1_wallet = function.id_generator();

    ID_l1_motor_on = function.id_generator();
    ID_l1_motor_off = function.id_generator();
    ID_l1_motor_visibility = function.id_generator();
    ID_l1_motor_speed = function.id_generator();
    ID_l1_motor_speed_visibility = function.id_generator();

    ID_l1_sock_client_port = function.id_generator();
    ID_l1_sock_client_port_visibility = function.id_generator();

    ID_l1_stat_packet = function.id_generator();
    ID_l1_stat_visibility = function.id_generator();
    ID_l1_throughtput_value = function.id_generator();
    ID_l1_throughtput_range = function.id_generator();

    # LiDAR 2
    ID_l2_line_visibility = function.id_generator();
    ID_l2_status = function.id_generator();
    ID_l2_status_light = function.id_generator();
    ID_l2_activated = function.id_generator();
    ID_l2_ip = function.id_generator();
    ID_l2_ip_visibility = function.id_generator();
    ID_l2_wallet = function.id_generator();

    ID_l2_motor_on = function.id_generator();
    ID_l2_motor_off = function.id_generator();
    ID_l2_motor_visibility = function.id_generator();
    ID_l2_motor_speed = function.id_generator();
    ID_l2_motor_speed_visibility = function.id_generator();

    ID_l2_sock_client_port = function.id_generator();
    ID_l2_sock_client_port_visibility = function.id_generator();

    ID_l2_stat_packet = function.id_generator();
    ID_l2_stat_visibility = function.id_generator();
    ID_l2_throughtput_value = function.id_generator();
    ID_l2_throughtput_range = function.id_generator();

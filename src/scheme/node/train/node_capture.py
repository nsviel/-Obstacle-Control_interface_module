#---------------------------------------------
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Data acquisition", tag="node_capture"):
        scheme_function.add_image("icon_computer", "icon_computer_visible")
        scheme_function.add_status(object.object.capture.ID_status_light, object.object.capture.ID_status)
        scheme_function.add_ip_wallet(object.object.capture.ID_wallet, object.object.capture.ID_ip, "-", object.object.capture.ID_ip_visibility)
        scheme_function.add_nb_thread(object.object.capture.ID_thread, object.object.capture.ID_thread_visibility)
        scheme_function.add_port_fixe_i(object.object.capture.ID_sock_server_l1, object.object.capture.ID_sock_server_l1_port, object.object.capture.ID_sock_server_l1_port_visibility)
        scheme_connection.add_sock_client_o_(object.object.capture.ID_sock_client_l1)
        scheme_function.add_port_fixe_i(object.object.capture.ID_sock_server_l2, object.object.capture.ID_sock_server_l2_port, object.object.capture.ID_sock_server_l2_port_visibility)
        scheme_connection.add_sock_client_o_(object.object.capture.ID_sock_client_l2)
        scheme_function.add_lidar_device(object.object.capture.ID_device_l1, object.object.capture.ID_device_l2, object.object.capture.ID_device_visibility)
        scheme_connection.add_http_server_o(object.object.capture.ID_http_server)
        scheme_function.add_port_fixe(object.object.capture.ID_http_server_port, object.object.capture.ID_http_server_port_visibility)

#---------------------------------------------
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Data processing", tag="node_slam"):
        scheme_function.add_status(object.slam.ID_status_light, object.slam.ID_status)
        scheme_function.add_ip_wallet(object.slam.ID_wallet, object.slam.ID_ip, "localhost", object.slam.ID_ip_visibility)
        scheme_function.add_velo_option(object.slam.ID_setting_with_slam, object.slam.ID_setting_cam_view, object.slam.ID_setting_reset)
        scheme_connection.add_sock_server_o(object.slam.ID_sock_server)
        scheme_function.add_port_fixe(object.slam.ID_sock_server_port, object.slam.ID_sock_server_port_visibility)
        scheme_connection.add_http_server_o(object.slam.ID_http_server)
        scheme_function.add_port_fixe(object.slam.ID_http_server_port, object.slam.ID_http_server_port_visibility)

#---------------------------------------------
from src.scheme import scheme_function
from src.scheme import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="cloud_car", tag="node_cloud_car"):
        scheme_function.add_ip("va_ip")
        scheme_connection.add_http_client_i("va_http_client")

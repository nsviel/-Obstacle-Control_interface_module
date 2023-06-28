#---------------------------------------------
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="AI", tag="node_ai"):
        scheme_function.add_status("ai_status_but", "ai_status")
        scheme_function.add_ip_wallet("ai_wallet", "ai_ip", "localhost", "ai_ip_visible")
        scheme_function.add_ai_param_height("ai_lidar_height")
        scheme_function.add_ai_param_thres("ai_threshold")
        scheme_connection.add_http_server_o("ai_http_server")
        scheme_function.add_port_fixe("ai_http_server_port", "ai_http_port_visible")

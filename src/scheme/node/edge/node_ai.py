#---------------------------------------------
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="AI", tag="node_ai"):
        scheme_function.add_status(object.ai.ID_status_light, object.ai.ID_status)
        scheme_function.add_ip_wallet(object.ai.ID_wallet, object.ai.ID_ip, "localhost", object.ai.ID_ip_visibility)
        scheme_function.add_ai_param_height(object.ai.ID_setting_lidar_height)
        scheme_function.add_ai_param_thres(object.ai.ID_setting_threshold)
        scheme_connection.add_http_server_o(object.ai.ID_http_server)
        scheme_function.add_port_fixe(object.ai.ID_http_server_port, object.ai.ID_http_server_port_visibility)

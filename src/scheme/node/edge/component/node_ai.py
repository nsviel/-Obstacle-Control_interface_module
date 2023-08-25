#---------------------------------------------
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="AI", tag="node_ai"):
        scheme_function.add_status(object.object.edge_1.ai.ID_status_light, object.object.edge_1.ai.ID_status)
        scheme_function.add_ip_wallet(object.object.edge_1.ai.ID_wallet, object.object.edge_1.ai.ID_ip, "localhost", object.object.edge_1.ai.ID_ip_visibility)
        scheme_function.add_ai_param_height(object.object.edge_1.ai.ID_setting_lidar_height)
        scheme_function.add_ai_param_thres(object.object.edge_1.ai.ID_setting_threshold)
        scheme_connection.add_http_server_o(object.object.edge_1.ai.ID_http_server)
        scheme_function.add_port_fixe(object.object.edge_1.ai.ID_http_server_port, object.object.edge_1.ai.ID_http_server_port_visibility)

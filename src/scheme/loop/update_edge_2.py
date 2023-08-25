#---------------------------------------------
from src.param import param_interface
from src.scheme.link import scheme_link
from src.scheme.node.edge.data import scheme_plot
from src.scheme.style import scheme_color
from src.scheme.style import scheme_theme
from src.scheme.object import object
from src.utils import signal
from src.utils import io
from src import loop

import dearpygui.dearpygui as dpg


def update():
    update_edge()
    update_slam()
    update_ai()
    update_data()

def update_edge():
    if(param_interface.state_edge_2["self"]["lidar_main"] == "lidar_1"):
        s1 = "lidar_1"
        s2 = "lidar_2"
    elif(param_interface.state_edge_2["self"]["lidar_main"] == "lidar_2"):
        s1 = "lidar_2"
        s2 = "lidar_1"

    dpg.set_value(object.object.edge_2.ID_wallet, param_interface.state_control["edge_2"]["add"])
    dpg.set_value(object.object.edge_2.ID_status, param_interface.status_edge_2)
    dpg.set_value(object.object.edge_2.ID_ip, param_interface.state_edge_2["self"]["ip"])
    dpg.set_value(object.object.edge_2.ID_thread, param_interface.state_edge_2["self"]["nb_thread"])
    dpg.set_value(object.object.edge_2.ID_ip, param_interface.state_edge_2["self"]["edge_id"])
    dpg.set_value(object.object.edge_2.ID_sock_server_l1_port, param_interface.state_edge_2["self"]["sock_server_l1_port"])
    dpg.set_value(object.object.edge_2.ID_sock_server_l2_port, param_interface.state_edge_2["self"]["sock_server_l2_port"])
    dpg.set_value(object.object.edge_2.ID_http_server_port, param_interface.state_edge_2["self"]["http_server_port"])
    dpg.set_value(object.object.edge_2.ID_sock_client_l1_lidar_main, s1)
    dpg.set_value(object.object.edge_2.ID_sock_client_l2_source, s2)
    dpg.set_value(object.object.edge_2.ID_edge_id, param_interface.state_control["edge_2"]["edge_id"])
    dpg.set_value(object.object.edge_2.ID_edge_country, param_interface.state_control["edge_2"]["country"])
def update_slam():
    dpg.set_value(object.object.edge_1.slam.ID_ip, param_interface.state_edge_2["component_process"]["ip"])
    dpg.set_value(object.object.edge_1.slam.ID_sock_server_port, param_interface.state_edge_2["component_process"]["sock_server_port"])
    dpg.set_value(object.object.edge_1.slam.ID_http_server_port, param_interface.state_edge_2["component_process"]["http_server_port"])
def update_ai():
    dpg.set_value(object.object.edge_1.ai.ID_http_server_port, param_interface.state_edge_2["component_ai"]["http_server_port"])
def update_data():
    dpg.set_value("nb_frame", param_interface.state_edge_2["data"]["nb_frame"])
    dpg.set_value("nb_prediction", param_interface.state_edge_2["data"]["nb_prediction"])

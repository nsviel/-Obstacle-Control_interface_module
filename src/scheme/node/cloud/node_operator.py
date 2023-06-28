#---------------------------------------------
from src.param import param_interface
from src.scheme.style import scheme_function
from src.scheme.style import scheme_connection

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Train operator", tag="node_operator"):
        scheme_function.add_status("trainope_status_but", "trainope_status")
        scheme_function.add_ip_wallet("trainope_wallet", "ip_operator", param_interface.state_edge_1["train_operator"]["add"], "ip_operator_visible")
        scheme_function.add_input("MQTT", "trainope_mqtt_broker")
        scheme_function.add_port_trainope("trainope_broker_port", "ai_trainope_port_visible")
        scheme_function.add_mqtt_topic("trainope_mqtt_topic", "trainope_mqtt_topic_visible")

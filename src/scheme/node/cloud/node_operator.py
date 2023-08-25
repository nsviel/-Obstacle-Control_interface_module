#---------------------------------------------
from src.param import param_interface
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.object import object

import dearpygui.dearpygui as dpg


def design_node():
    with dpg.node(label="Train operator", tag="node_operator"):
        scheme_function.add_status(object.object.operator.ID_status_light, object.object.operator.ID_status)
        scheme_function.add_ip_wallet(object.object.operator.ID_wallet, object.object.operator.ID_ip, param_interface.state_edge_1["cloud_operator"]["add"], object.object.operator.ID_ip_visibility)
        scheme_function.add_input("MQTT", object.object.operator.ID_mqtt_broker)
        scheme_function.add_port_trainope(object.object.operator.ID_mqtt_broker_port, object.object.operator.ID_mqtt_broker_port_visibility)
        scheme_function.add_mqtt_topic(object.object.operator.ID_mqtt_topic, object.object.operator.ID_mqtt_topic_visibility)

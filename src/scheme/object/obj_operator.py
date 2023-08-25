#---------------------------------------------
from src.utils import function


class Operator:
    # Info
    ID_status = function.id_generator();
    ID_status_light = function.id_generator();
    ID_ip = function.id_generator();
    ID_ip_visibility = function.id_generator();
    ID_wallet = function.id_generator();

    # MQTT
    ID_mqtt_broker = function.id_generator();
    ID_mqtt_broker_port = function.id_generator();
    ID_mqtt_broker_port_visibility = function.id_generator();
    ID_mqtt_topic = function.id_generator();
    ID_mqtt_topic_visibility = function.id_generator();

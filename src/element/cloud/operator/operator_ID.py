#---------------------------------------------
from src.utils import function
from src.gui.background import texture


class Operator_ID:
    def __init__(self):
        self.name = "Train operator"
        self.ID = "operator"
        self.init_ID_node()
        self.init_ID_info()
        self.init_ID_mqtt()

    def init_ID_node(self):
        self.ID_node = function.id_generator();
        self.ID_node_handler = function.id_generator();
        self.ID_node_coord = function.id_generator();

    def init_ID_info(self):
        self.ID_window_table_info = function.id_generator();
        self.ID_window = function.id_generator();
        self.ID_status = function.id_generator();
        self.ID_status_light = function.id_generator();
        self.ID_ip = function.id_generator();
        self.ID_ip_visibility = function.id_generator();
        self.ID_wallet = function.id_generator();

    def init_ID_mqtt(self):
        self.ID_mqtt_broker = function.id_generator();
        self.ID_mqtt_broker_port = function.id_generator();
        self.ID_mqtt_broker_port_visibility = function.id_generator();
        self.ID_mqtt_topic = function.id_generator();
        self.ID_mqtt_topic_visibility = function.id_generator();

    def init_ID_icon(self):
        self.ID_icon_hub = texture.load_texture("train")

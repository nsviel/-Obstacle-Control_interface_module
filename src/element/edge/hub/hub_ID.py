#---------------------------------------------
from src.utils import function
from src.gui.background import gui_texture


class Hub_ID:
    def __init__(self, ID_edge):
        self.ID_edge = ID_edge
        self.name = "Hub"
        self.ID = "hub"
        self.init_ID_node()
        self.init_ID_info()
        self.init_ID_http()
        self.init_mqtt_ID()
        self.init_ID_socket()
        self.init_ID_parameter()

    def init_ID_node(self):
        self.ID_node = function.id_generator();
        self.ID_node_handler = function.id_generator();
        self.ID_node_coord = function.id_generator();

    def init_ID_info(self):
        self.ID_window_table_info = function.id_generator();
        self.ID_window_info = function.id_generator();
        self.ID_window_parameter = function.id_generator();
        self.ID_status = function.id_generator();
        self.ID_status_light = function.id_generator();
        self.ID_ip = function.id_generator();
        self.ID_edge_id = function.id_generator();
        self.ID_edge_country = function.id_generator();
        self.ID_wallet = function.id_generator();
        self.ID_thread = function.id_generator();
        self.ID_table = function.id_generator();

    def init_ID_http(self):
        self.ID_http_client = function.id_generator();
        self.ID_http_server = function.id_generator();
        self.ID_http_server_port = function.id_generator();

    def init_mqtt_ID(self):
        self.ID_mqtt_client = function.id_generator();
        self.ID_mqtt_client_name = function.id_generator();

    def init_ID_socket(self):
        self.ID_sock_server_l1 = function.id_generator();
        self.ID_sock_server_l1_port = function.id_generator();
        self.ID_sock_client_l1 = function.id_generator();

        self.ID_sock_server_l2 = function.id_generator();
        self.ID_sock_server_l2_port = function.id_generator();
        self.ID_sock_client_l2 = function.id_generator();
        self.ID_sock_client_l2_source = function.id_generator();

        self.ID_combo_lidar_source = function.id_generator();
        self.ID_source_1 = function.id_generator();
        self.ID_source_2 = function.id_generator();

    def init_ID_parameter(self):
        self.ID_setting_lidar_height = function.id_generator();
        self.ID_setting_threshold = function.id_generator();

    def init_ID_icon(self):
        self.ID_icon_hub = gui_texture.load_texture("hub")

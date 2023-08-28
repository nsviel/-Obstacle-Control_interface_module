#---------------------------------------------
from src.utils import function
from src.gui.background import texture


class Ai_ID:
    def __init__(self, ID_edge):
        self.ID_edge = ID_edge
        self.name = "AI"
        self.ID = "ai"
        self.init_ID_node()
        self.init_ID_info()
        self.init_ID_http()
        self.init_ID_parameter()

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

    def init_ID_http(self):
        self.ID_http_server = function.id_generator();
        self.ID_http_server_port = function.id_generator();
        self.ID_http_server_port_visibility = function.id_generator();

    def init_ID_parameter(self):
        self.ID_setting_lidar_height = function.id_generator();
        self.ID_setting_threshold = function.id_generator();

    def init_ID_icon(self):
        self.ID_icon_gear = texture.load_texture("gear")

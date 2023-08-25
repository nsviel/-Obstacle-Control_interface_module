#---------------------------------------------
from src.utils import function
from src.scheme.object import edge_link
from src.scheme.object import obj_ai
from src.scheme.object import obj_slam


class Edge:
    def __init__(self):
        self.init_ID()
        self.init_object()

    def init_object(self):
        self.link = edge_link.Edge_link()
        self.slam = obj_slam.SLAM()
        self.ai = obj_ai.AI()

    def init_ID(self):
        # Info
        self.ID_node = function.id_generator();
        self.ID_status = function.id_generator();
        self.ID_status_light = function.id_generator();
        self.ID_ip = function.id_generator();
        self.ID_ip_visibility = function.id_generator();
        self.ID_edge_id = function.id_generator();
        self.ID_edge_id_visibility = function.id_generator();
        self.ID_edge_country = function.id_generator();
        self.ID_wallet = function.id_generator();
        self.ID_thread = function.id_generator();
        self.ID_thread_visibility = function.id_generator();

        # HTTP
        self.ID_http_client_i = function.id_generator();
        self.ID_http_client_o = function.id_generator();
        self.ID_http_server_o = function.id_generator();
        self.ID_http_server_port = function.id_generator();
        self.ID_http_server_port_visibility = function.id_generator();

        # MQTT
        self.ID_mqtt_client = function.id_generator();
        self.ID_mqtt_client_name = function.id_generator();
        self.ID_mqtt_visibility = function.id_generator();

        # Socket
        self.ID_sock_server_l1_i = function.id_generator();
        self.ID_sock_server_l1_o = function.id_generator();
        self.ID_sock_server_l1_port = function.id_generator();
        self.ID_sock_server_l1_port_visibility = function.id_generator();
        self.ID_sock_client_l1_i = function.id_generator();
        self.ID_sock_client_l1_o = function.id_generator();
        self.ID_sock_client_l1_lidar_main = function.id_generator();

        self.ID_sock_server_l2_i = function.id_generator();
        self.ID_sock_server_l2_port = function.id_generator();
        self.ID_sock_server_l2_port_visibility = function.id_generator();
        self.ID_sock_client_l2_o = function.id_generator();
        self.ID_sock_client_l2_source = function.id_generator();

        self.ID_source_1 = function.id_generator();
        self.ID_source_2 = function.id_generator();

        # Setting
        self.ID_setting_lidar_height = function.id_generator();
        self.ID_setting_threshold = function.id_generator();

    name = "Edge"
    country = ""
    ID = 0
    link = []
    ai = []
    slam = []

#---------------------------------------------
from src.utils import function
from src.gui.background import texture


class Network_ID:
    def __init__(self, ID_edge):
        self.ID_edge = ID_edge
        self.name = "Network"
        self.ID = "network"
        self.init_ID_node()
        self.init_ID_info()
        self.init_ID_perf()
        self.init_ID_mongo()

    def init_ID_node(self):
        self.ID_node = function.id_generator();
        self.ID_node_handler = function.id_generator();
        self.ID_node_coord = function.id_generator();

    def init_ID_info(self):
        self.ID_status = function.id_generator();
        self.ID_status_light = function.id_generator();
        self.ID_window_info = function.id_generator();
        self.ID_window_parameter = function.id_generator();
        self.ID_window_table_info = function.id_generator();

    def init_ID_perf(self):
        self.ID_perf_throughput_up = function.id_generator();
        self.ID_perf_latency_up = function.id_generator();
        self.ID_perf_latency_down = function.id_generator();
        self.ID_perf_reliability_up = function.id_generator();
        self.ID_perf_reliability_down = function.id_generator();
        self.ID_perf_time_interruption = function.id_generator();
        self.ID_perf_time_processing = function.id_generator();

    def init_ID_mongo(self):
        self.ID_mongo_status_light = function.id_generator();
        self.ID_mongo_table = function.id_generator();
        self.ID_mongo_ip = function.id_generator();
        self.ID_mongo_port = function.id_generator();
        self.ID_mongo_db = function.id_generator();
        self.ID_mongo_collection = function.id_generator();
        self.ID_mongo_username = function.id_generator();
        self.ID_mongo_password = function.id_generator();
        self.ID_mongo_nb_data = function.id_generator();

    def init_ID_icon(self):
        self.ID_icon_network = texture.load_texture("wifi")
        self.ID_icon_database = texture.load_texture("database")

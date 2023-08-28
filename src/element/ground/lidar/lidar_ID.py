#---------------------------------------------
from src.utils import function
from src.gui.background import texture


class Lidar_ID:
    def __init__(self, ID):
        self.name = "lidar_" + str(ID)
        self.ID = ID
        self.init_ID_node()
        self.init_ID_info()
        self.init_ID_motor()
        self.init_ID_connection()

    def init_ID_node(self):
        self.ID_node = function.id_generator();
        self.ID_node_handler = function.id_generator();
        self.ID_node_coord = function.id_generator();

    def init_ID_info(self):
        self.ID_window_table_info = function.id_generator();
        self.ID_window = function.id_generator();
        self.ID_status = function.id_generator();
        self.ID_status_light = function.id_generator();
        self.ID_activated = function.id_generator();
        self.ID_ip = function.id_generator();
        self.ID_wallet = function.id_generator();
        self.ID_stat_packet = function.id_generator();
        self.ID_throughtput_value = function.id_generator();
        self.ID_throughtput_range = function.id_generator();
        self.ID_device = function.id_generator();
        self.ID_device_list = function.id_generator();

    def init_ID_motor(self):
        self.ID_motor_on = function.id_generator();
        self.ID_motor_off = function.id_generator();
        self.ID_motor_speed = function.id_generator();

    def init_ID_connection(self):
        self.ID_sock_client = function.id_generator();
        self.ID_sock_client_port = function.id_generator();

    def init_ID_icon(self):
        self.ID_icon_lidar = texture.load_texture("lidar")

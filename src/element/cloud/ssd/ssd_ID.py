#---------------------------------------------
from src.utils import function
from src.gui.background import gui_texture


class Ssd_ID:
    def __init__(self):
        self.name = "SSD"
        self.ID = "ssd"
        self.init_ID_node()
        self.init_ID_info()
        self.init_ID_path()

    def init_ID_node(self):
        self.ID_node = function.id_generator();
        self.ID_node_coord = function.id_generator();
        self.ID_node_handler = function.id_generator();
        self.ID_node_input = function.id_generator();

    def init_ID_info(self):
        self.ID_window_table_info = function.id_generator();
        self.ID_window_info = function.id_generator();
        self.ID_window_parameter = function.id_generator();
        self.ID_status = function.id_generator();
        self.ID_status_light = function.id_generator();
        self.ID_activated = function.id_generator();
        self.ID_parameter_visibility = function.id_generator();
        self.ID_memory_used = function.id_generator();
        self.ID_memory_total = function.id_generator();

    def init_ID_path(self):
        self.ID_file_name = function.id_generator();
        self.ID_path = function.id_generator();
        self.ID_path_add = function.id_generator();

        self.ID_file_l1_size = function.id_generator();
        self.ID_path_l1 = function.id_generator();
        self.ID_path_l1_visibility = function.id_generator();

        self.ID_file_l2_size = function.id_generator();
        self.ID_path_l2 = function.id_generator();
        self.ID_path_l2_visibility = function.id_generator();

    def init_ID_icon(self):
        self.ID_icon_hub = gui_texture.load_texture("hdd")

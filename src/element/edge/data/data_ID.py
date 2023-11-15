#---------------------------------------------
from src.utils import function
from src.gui.background import gui_texture


class Data_ID:
    def __init__(self, ID_edge):
        self.ID_edge = ID_edge
        self.name = "Data"
        self.ID = "data"
        self.init_ID_node()
        self.init_ID_info()
        self.init_ID_stats()
        self.init_ID_plot()

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

    def init_ID_stats(self):
        self.ID_nb_frame = function.id_generator();
        self.ID_nb_prediction = function.id_generator();

    def init_ID_plot(self):
        self.ID_yaxis_l1 = function.id_generator();
        self.ID_yaxis_l2 = function.id_generator();
        self.ID_plot_l1 = function.id_generator();
        self.ID_plot_l2 = function.id_generator();

    def init_ID_icon(self):
        self.ID_image = gui_texture.load_texture("image_empty")

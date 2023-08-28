#---------------------------------------------
from src.utils import function


class Wallet_ID:
    def __init__(self):
        self.name = "Wallet"
        self.ID = "wallet"
        self.init_ID_info()
        self.init_ID_table()

    def init_ID_info(self):
        self.ID_window_table_info = function.id_generator();
        self.ID_window = function.id_generator();
        self.ID_status = function.id_generator();
        self.ID_node_coord = function.id_generator();

    def init_ID_table(self):
        self.ID_table = function.id_generator();
        self.ID_new_address = function.id_generator();
        self.ID_new_ip = function.id_generator();

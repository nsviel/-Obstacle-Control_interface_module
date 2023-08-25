#---------------------------------------------
from src.utils import function
from src.gui.background import texture


class Block_ID:
    def __init__(self):
        self.init_ID_setting()
        self.init_ID_block()
        self.init_ID_legend()

    def init_ID_setting(self):
        self.ID_is_visible = "ID_block_visible"

    def init_ID_block(self):
        self.ID_block_ground = function.id_generator();
        self.ID_block_edge = function.id_generator();
        self.ID_block_cloud = function.id_generator();
        self.ID_block_legend = function.id_generator();

    def init_ID_legend(self):
        self.ID_legend_ground = function.id_generator();
        self.ID_legend_edge = function.id_generator();
        self.ID_legend_cloud = function.id_generator();
        self.ID_legend_control = function.id_generator();

    def init_ID_icon(self):
        self.ID_icon_ground = texture.load_texture("train")
        self.ID_icon_edge = texture.load_texture("server")
        self.ID_icon_cloud = texture.load_texture("cloud")

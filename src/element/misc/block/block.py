#---------------------------------------------
from src.element.misc.block import block_ID
from src.element.misc.block import block_ground
from src.element.misc.block import block_edge
from src.element.misc.block import block_cloud
from src.gui.background import gui_ID
from src.gui.style import colorization
import dearpygui.dearpygui as dpg


class Block:
    def __init__(self):
        self.ID = block_ID.Block_ID()
        self.ground = block_ground.Block_ground(self.ID)
        self.edge = block_edge.Block_edge(self.ID)
        self.cloud = block_cloud.Block_cloud(self.ID)

    def design_blocks(self):
        self.ID.init_ID_icon()
        self.ground.design_block()
        self.edge.design_block()
        self.cloud.design_block()
        self.colorize_blocks()
        self.switch_visibility()

    def switch_visibility(self):
        what = dpg.get_value(gui_ID.ID_block_visibility)
        self.ground.set_visibility(what)
        self.edge.set_visibility(what)
        self.cloud.set_visibility(what)
        self.position_blocks()

    def colorize_blocks(self):
        colorization.colorize_item(gui_ID.ID_block_visibility, "checkbox")
        colorization.colorize_blocks(self.ID.ID_block_ground, "ground")
        colorization.colorize_blocks(self.ID.ID_block_edge, "edge")
        colorization.colorize_blocks(self.ID.ID_block_cloud, "cloud")

    def position_blocks(self):
        coord_block_ground = [10, 10]
        coord_block_edge = [600, 10]
        coord_block_cloud = [1075, 10]
        dpg.set_item_pos(self.ID.ID_block_ground, coord_block_ground)
        dpg.set_item_pos(self.ID.ID_block_edge, coord_block_edge)
        dpg.set_item_pos(self.ID.ID_block_cloud, coord_block_cloud)

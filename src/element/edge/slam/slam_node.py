#---------------------------------------------
from src.param import param_control
from src.base import node
from src.gui.style import colorization
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Slam_node(node.Node):
    # Build function
    def build(self):
        self.ID.init_ID_icon()
        with dpg.node(label=self.ID.name, tag=self.ID.ID_node):
            # Icone & status button
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.table(header_row=False, borders_innerH=False, policy=dpg.mvTable_SizingFixedFit):
                    dpg.add_table_column(label="Icone", width_fixed=True, init_width_or_weight=75)
                    dpg.add_table_column(label="Button", width_fixed=True, init_width_or_weight=15)
                    with dpg.table_row():
                        dpg.add_image(self.ID.ID_icon_gear, width=15, height=15)
                        dpg.add_button(tag=self.ID.ID_status_light, width=15)
                with dpg.drawlist(width=100, height=1):
                    dpg.draw_line([0, 0], [125, 0], color=gui_color.color_line)

            # Connection
            with dpg.node_attribute(tag=self.ID.ID_sock_server, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket");
                    dpg.add_text("server", color=gui_color.color_node_sub);
                    dpg.add_text(1, tag=self.ID.ID_sock_server_port, color=gui_color.color_node_value);
                with dpg.drawlist(width=100, height=1):
                    dpg.draw_line([0, 0], [125, 0], color=gui_color.color_line)
            with dpg.node_attribute(tag=self.ID.ID_http_server, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("HTTPS");
                    dpg.add_text("server", color=gui_color.color_node_sub);
                    dpg.add_text(1, tag=self.ID.ID_http_server_port, color=gui_color.color_node_value);
            #dpg.configure_item(self.ID.ID_wallet, items=param_control.wallet_add)
        self.position_node()
        self.colorize_node()
    def position_node(self):
        pose = parser_json.get_pos_from_json()
        dpg.set_item_pos(self.ID.ID_node, pose["edge"]["slam"])
    def colorize_node(self):
        colorization.colorize_item(self.ID.ID_setting_with_slam, "checkbox")
        colorization.colorize_node(self.ID.ID_node, "edge")

    # Update function
    def update(self):
        colorization.colorize_status_light(self.ID.ID_status_light, param_control.state_edge["hub"]["interface"]["slam_http_connected"])
        dpg.set_value(self.ID.ID_sock_server_port, param_control.state_edge["slam"]["socket"]["server_port"])
        dpg.set_value(self.ID.ID_http_server_port, param_control.state_edge["slam"]["http"]["server_port"])

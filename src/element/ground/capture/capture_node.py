#---------------------------------------------
from src.param import param_control
from src.base import node
from src.gui.style import colorization
from src.gui.style import gui_color
from src.gui.background import gui_ID
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Capture_node(node.Node):
    # Build
    def build(self):
        self.ID.init_ID_icon()
        with dpg.node(label=self.ID.name, tag=self.ID.ID_node):
            # Icone & status button
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.table(header_row=False, borders_innerH=False, policy=dpg.mvTable_SizingFixedFit):
                    dpg.add_table_column(label="Icone", width_fixed=True, init_width_or_weight=75)
                    dpg.add_table_column(label="Button", width_fixed=True, init_width_or_weight=15)
                    with dpg.table_row():
                        dpg.add_image(self.ID.ID_icon_capture, width=25, height=15)
                        dpg.add_button(tag=self.ID.ID_status_light, width=15)
                with dpg.drawlist(width=100, height=1):
                    dpg.draw_line([0, 0], [125, 0], color=gui_color.color_line)

            # Socket
            with dpg.node_attribute(tag=self.ID.ID_sock_server_l1, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket");
                    dpg.add_text("server", color=gui_color.color_info);
                    dpg.add_text(1, tag=self.ID.ID_sock_server_l1_port, color=gui_color.color_port);
            with dpg.node_attribute(tag=self.ID.ID_sock_client_l1, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket");
                    dpg.add_text("client", color=gui_color.color_info);
                with dpg.drawlist(width=100, height=1):
                    dpg.draw_line([0, 0], [125, 0], color=gui_color.color_line)
            with dpg.node_attribute(tag=self.ID.ID_sock_server_l2, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket");
                    dpg.add_text("server", color=gui_color.color_info);
                    dpg.add_text(1, tag=self.ID.ID_sock_server_l2_port, color=gui_color.color_port);
            with dpg.node_attribute(tag=self.ID.ID_sock_client_l2, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket");
                    dpg.add_text("client", color=gui_color.color_info);
                with dpg.drawlist(width=100, height=1):
                    dpg.draw_line([0, 0], [125, 0], color=gui_color.color_line)

            # HTTPS
            with dpg.node_attribute(tag=self.ID.ID_http_server, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("HTTPS");
                    dpg.add_text("server", color=gui_color.color_info);
                    dpg.add_text(1, tag=self.ID.ID_http_server_port, color=gui_color.color_port);
            #dpg.configure_item(self.ID.ID_wallet, items=param_control.wallet_add)
        self.position_node()

    def position_node(self):
        data = parser_json.get_pos_from_json()
        dpg.set_item_pos(self.ID.ID_node, data["ground"]["capture"])

    def update_node(self):
        colorization.colorize_status(self.ID.ID_status_light, param_control.status_capture)
        dpg.set_value(self.ID.ID_http_server_port, int(param_control.state_capture["self"]["http_server_port"]))
        dpg.set_value(self.ID.ID_sock_server_l1_port, param_control.state_capture["self"]["l1_port"])
        dpg.set_value(self.ID.ID_sock_server_l2_port, param_control.state_capture["self"]["l2_port"])

    def colorize_node(self):
        colorization.colorize_item(self.ID.ID_http_server_port, input_text)
        colorization.colorize_item(self.ID.ID_wallet, input_text)
        colorization.colorize_item(self.ID.ID_ip, input_text)

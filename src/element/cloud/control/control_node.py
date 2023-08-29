#---------------------------------------------
from src.param import param_control
from src.base import node
from src.gui.style import colorization
from src.gui.style import gui_color
from src.utils import parser_json
from src.connection.HTTPS import https_client_post
from src import daemon
import dearpygui.dearpygui as dpg


class Control_node(node.Node):
    # Build function
    def build(self):
        self.ID.init_ID_icon()
        with dpg.node(label=self.ID.name, tag=self.ID.ID_node):
            # Icone & status button
            with dpg.node_attribute(tag=self.ID.ID_ssd_connection, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.table(header_row=False, borders_innerH=False, policy=dpg.mvTable_SizingFixedFit):
                    dpg.add_table_column(label="Icone", width_fixed=True, init_width_or_weight=75)
                    dpg.add_table_column(label="Button", width_fixed=True, init_width_or_weight=15)
                    with dpg.table_row():
                        dpg.add_image(self.ID.ID_icon, width=10, height=15)
                        dpg.add_button(tag=self.ID.ID_status_light, width=15)
                with dpg.drawlist(width=100, height=1):
                    dpg.draw_line([0, 0], [125, 0], color=gui_color.color_line)

            # Socket
            with dpg.node_attribute(tag=self.ID.ID_sock_server_l1, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket");
                    dpg.add_text("server", color=gui_color.color_node_sub);
                    dpg.add_input_int(tag=self.ID.ID_sock_server_l1_port, default_value=1, width=75, callback=self.update_sock_port);
            with dpg.node_attribute(tag=self.ID.ID_sock_server_l2, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("Socket");
                    dpg.add_text("server", color=gui_color.color_node_sub);
                    dpg.add_input_int(tag=self.ID.ID_sock_server_l2_port, default_value=1, width=75, callback=self.update_sock_port);

            # HTTPS
            with dpg.node_attribute(tag=self.ID.ID_http_client, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("HTTPS");
                    dpg.add_text("client", color=gui_color.color_node_sub);
        self.position_node()
        self.colorize_node()
    def position_node(self):
        pose = parser_json.get_pos_from_json()
        dpg.set_item_pos(self.ID.ID_node, pose["cloud"]["control"])
    def colorize_node(self):
        colorization.colorize_item(self.ID.ID_sock_server_l1_port, "node_value")
        colorization.colorize_item(self.ID.ID_sock_server_l2_port, "node_value")
        colorization.colorize_node(self.ID.ID_node, "cloud")

    # Update function
    def update(self):
        colorization.colorize_status(self.ID.ID_status_light, True)
    def update_node(self):
        dpg.set_value(self.ID.ID_status, param_control.state_control["control"]["info"]["status"])
        dpg.set_value(self.ID.ID_ip, param_control.state_control["control"]["ip"])
        dpg.set_value(self.ID.ID_thread, param_control.state_control["control"]["nb_thread"])
        dpg.set_value(self.ID.ID_sock_server_l1_port, param_control.state_control["control"]["socket"]["server_l1_port"])
        dpg.set_value(self.ID.ID_sock_server_l2_port, param_control.state_control["control"]["socket"]["server_l2_port"])
        dpg.set_value(self.ID.ID_temperature, signal.get_temps_core(0))
    def update_sock_port(self):
        l1_port = dpg.get_value(self.ID.ID_sock_server_l1_port)
        l2_port = dpg.get_value(self.ID.ID_sock_server_l2_port)
        if(l1_port != l2_port and l1_port > 0 and l2_port > 0):
            param_control.state_control["control"]["socket"]["server_l1_port"] = l1_port
            param_control.state_control["control"]["socket"]["server_l2_port"] = l2_port
            daemon.daemon_socket_l1.restart_daemon()
            daemon.daemon_socket_l2.restart_daemon()

            param_control.state_edge["interface"]["control"]["socket"]["server_l1_port"] = dpg.get_value(self.ID.ID_sock_server_l1_port)
            param_control.state_edge["interface"]["control"]["socket"]["server_l2_port"] = dpg.get_value(self.ID.ID_sock_server_l2_port)
            https_client_post.post_state("edge", param_control.state_edge)

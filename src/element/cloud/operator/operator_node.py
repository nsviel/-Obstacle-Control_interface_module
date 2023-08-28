#---------------------------------------------
from src.param import param_control
from src.base import node
from src.gui.style import colorization
from src.gui.style import gui_color
from src.utils import parser_json
from src.connection.HTTPS import https_client_post
import dearpygui.dearpygui as dpg


class Operator_node(node.Node):
    def build(self):
        self.ID.init_ID_icon()
        with dpg.node(label=self.ID.name, tag=self.ID.ID_node):
            # Icone & status button
            with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                with dpg.table(header_row=False, borders_innerH=False, policy=dpg.mvTable_SizingFixedFit):
                    dpg.add_table_column(label="Icone", width_fixed=True, init_width_or_weight=75)
                    dpg.add_table_column(label="Button", width_fixed=True, init_width_or_weight=15)
                    with dpg.table_row():
                        dpg.add_image(self.ID.ID_icon_hub, width=15, height=15)
                        dpg.add_button(tag=self.ID.ID_status_light, width=15)
                with dpg.drawlist(width=100, height=1):
                    dpg.draw_line([0, 0], [125, 0], color=gui_color.color_line)

            # MQTT
            with dpg.node_attribute(tag=self.ID.ID_mqtt_broker, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.group(horizontal=True):
                    dpg.add_text("MQTT", color=gui_color.color_title);
                    dpg.add_input_int(tag=self.ID.ID_mqtt_broker_port, default_value=1, width=75, callback=self.callback_operator);
                with dpg.group(horizontal=True):
                    dpg.add_text("Topic");
                    dpg.add_input_text(tag=self.ID.ID_mqtt_topic, default_value="-", width=90, on_enter=True, callback=self.callback_operator)
            #dpg.configure_item(self.ID.ID_wallet, items=param_control.wallet_add)
        self.position_node()
        self.colorize_node()

    def position_node(self):
        data = parser_json.get_pos_from_json()
        dpg.set_item_pos(self.ID.ID_node, data["cloud"]["operator"])

    def update_node(self):
        dpg.set_value(self.ID.ID_status, param_control.status_operator)
        dpg.set_value(self.ID.ID_mqtt_broker_port, param_control.state_edge["cloud_operator"]["broker_port"])
        dpg.set_value(self.ID.ID_mqtt_topic, param_control.state_edge["cloud_operator"]["mqtt_topic"])

    def colorize_node(self):
        colorization.colorize_item(self.ID.ID_mqtt_broker_port, "node_value")
        colorization.colorize_item(self.ID.ID_mqtt_topic, "node_value")
        colorization.colorize_node(self.ID.ID_node, "cloud")

    def callback_operator(self):
        param_control.state_edge["cloud_operator"]["broker_port"] = dpg.get_value(self.ID.ID_mqtt_broker_port)
        param_control.state_edge["cloud_operator"]["mqtt_topic"] = dpg.get_value(self.ID.ID_mqtt_topic)
        param_control.state_edge["cloud_operator"]["mqtt_client"] = dpg.get_value(self.ID.ID_mqtt_client_name)
        https_client_post.post_state("edge", param_control.state_edge)
        https_client_post.post_param_value("edge", None, "cloud_operator", "reset")

    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["cloud"]["operator"] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)

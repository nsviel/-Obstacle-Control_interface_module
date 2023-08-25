#---------------------------------------------
from src.param import param_control
from src.element.base import window
from src.gui.background import gui_ID
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Lidar_window(window.Window):
    def build_parameter(self):
        with dpg.group(horizontal=True):
            dpg.add_text("Activated", color=gui_color.color_title);
            dpg.add_checkbox(tag=self.ID.ID_activated, label="", default_value=True, indent=75);
        with dpg.group(horizontal=True):
            dpg.add_button(label="ON ", tag=self.ID.ID_motor_on, width=50, callback=self.update_motor_start)
            dpg.add_button(label="OFF", tag=self.ID.ID_motor_off, width=50, callback=self.update_motor_stop)
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_input_text(tag=self.ID.ID_ip, label="", default_value="", width=150);
        with dpg.group(horizontal=True):
            dpg.add_text("Add:");
            dpg.add_combo(param_control.wallet_add, tag=self.ID.ID_wallet, label="", default_value="-", width=120, callback=self.update_ip)


        with dpg.group(horizontal=True):
            dpg.add_text("Speed:");
            dpg.add_input_int(tag=self.ID.ID_motor_speed, default_value=600, step=60, min_value=0, max_value=1200, width=75, min_clamped=True, max_clamped=True, callback=self.update_motor_speed);
            dpg.add_text("rpm");
        with dpg.group(horizontal=True):
            dpg.add_text("Packet:");
            dpg.add_text(0, tag=self.ID.ID_stat_packet, color=gui_color.color_info);
        with dpg.group(horizontal=True):
            dpg.add_text("Throughput:");
            dpg.add_text(0, tag=self.ID.ID_throughtput_value, color=gui_color.color_info);
            dpg.add_text("MB/s");
        with dpg.group(horizontal=True):
            dpg.add_text("[");
            dpg.add_text(0, tag=self.ID.ID_throughtput_range, color=gui_color.color_info);
            dpg.add_text("]");
            dpg.add_text("MB/s");
        with dpg.group():
            dpg.add_text("Device")
            dpg.add_listbox(tag=self.ID.ID_device_list, callback=self.update_device, width=125)

    def update_ip(self):
        ip = wallet_logic.get_ip_from_key(dpg.get_value(self.ID.ID_wallet))
        if(ip != None):
            param_control.state_capture[name]["ip"] = ip
            dpg.set_value(self.ID.ID_ip, ip)
            https_client_post.post_param_value("capture", self.ID.name, "ip", ip)

    # LiDAR motor
    def update_motor_start(self):
        https_client_post.post_param_value("capture", None, self.ID.name, "start")
    def update_motor_stop(self):
        https_client_post.post_param_value("capture", None, self.ID.name, "stop")
    def update_motor_speed(self):
        speed = dpg.get_value(self.ID.ID_motor_speed)
        param_control.state_capture[self.ID.name]["speed"] = speed
        https_client_post.post_param_value("capture", self.ID.name, "speed", speed)

    # Colorization
    def colorize_item(self):
        checkbox = gui_color.color_checkbox()
        input_text = gui_color.color_input_text()
        dpg.bind_item_theme(self.ID.ID_activated, checkbox)
        dpg.bind_item_theme(self.ID.ID_ip, input_text)
        dpg.bind_item_theme(self.ID.ID_motor_speed, input_text)
        dpg.bind_item_theme(self.ID.ID_sock_client_port, input_text)
        dpg.bind_item_theme(self.ID.ID_wallet, input_text)

        layer_sensor = gui_color.color_layer_train()
        dpg.bind_item_theme("lidar_1", layer_sensor)
        dpg.bind_item_theme("lidar_2", layer_sensor)
    def update_color(self):
        colorization.colorize_onoff(self.ID.ID_motor_on, self.ID.ID_motor_off, param_control.state_capture[self.ID.name]["running"])
        #colorization.colorize_status(ID.ID_status_light, lidar.status)

    # LiDAR node
    def update_state(self):
        param_control.state_capture[self.ID.name]["activated"] = dpg.get_value(self.ID.ID_activated)
        param_control.state_capture[self.ID.name]["ip"] = dpg.get_value(self.ID.ID_ip)
        param_control.state_capture[self.ID.name]["speed"] = dpg.get_value(self.ID.ID_motor_speed)
        param_control.state_capture[self.ID.name]["device"] = dpg.get_value(self.ID.ID_device)
        param_control.state_capture[self.ID.name]["port"] = dpg.get_value(self.ID.ID_sock_client_port)
        https_client_post.post_state("capture", param_control.state_capture)

    def update_value(self):
        dpg.set_value(self.ID.ID_stat_packet, param_control.state_capture[self.ID.name]["packet"]["value"])
        value = "%.2f"% param_control.state_capture[self.ID.name]["throughput"]["value"]
        min = param_control.state_capture[self.ID.name]["throughput"]["min"]
        mean = param_control.state_capture[self.ID.name]["throughput"]["mean"]
        max = param_control.state_capture[self.ID.name]["throughput"]["max"]
        range = "%.2f, %.2f, %.2f"% (min, mean, max)
        dpg.set_value(self.ID.ID_throughtput_value, value)
        dpg.set_value(self.ID.ID_throughtput_range, range)
        dpg.set_value(self.ID.ID_ip, param_control.state_capture[self.ID.name]["ip"])
        dpg.set_value(self.ID.ID_sock_client_port, param_control.state_capture[self.ID.name]["port"])
        dpg.set_value(self.ID.ID_wallet, param_control.state_capture[self.ID.name]["add"])
        dpg.configure_item(ID.ID_wallet, items=param_control.wallet_add)
    def update_device(self):
        device = dpg.get_value(self.ID.ID_device_list)
        https_client_post.post_param_value("capture", self.ID.name, "device", device)

    def save_coord_to_file(self):
        data = parser_json.get_pos_from_json()
        data["ground"][self.ID.name] = dpg.get_item_pos(self.ID.ID_node)
        parser_json.upload_file(param_control.path_node_coordinate, data)

#---------------------------------------------
from src.param import param_interface
from src.scheme.link import scheme_link
from src.scheme.node.edge.data import scheme_plot
from src.scheme.style import scheme_color
from src.scheme.style import scheme_theme
from src.scheme.object import object
from src.scheme.loop import update_edge_1
from src.scheme.loop import update_edge_2
from src.utils import signal
from src.utils import io
from src import loop

import dearpygui.dearpygui as dpg


def update_scheme():
    scheme_link.update_link_color()
    update_edge_1.update()
    update_edge_2.update()
    update_status()
    update_ssd()
    update_train()
    update_control()
    update_operator()
    update_capture()
    update_network()

def update_status():
    dpg.set_value(object.object.operator.ID_status, param_interface.status_operator)
    dpg.set_value(object.object.ssd.ID_status, param_interface.status_ssd)
    dpg.set_value(object.object.control.ID_status, param_interface.status_interface)
    dpg.set_value(object.object.edge_1.slam.ID_status, param_interface.status_processing)
    dpg.set_value(object.object.edge_1.ai.ID_status, param_interface.status_ai)
    dpg.set_value(object.object.capture.ID_status, param_interface.status_capture)
    dpg.set_value(object.object.edge_2.ID_status, param_interface.status_edge_2)

    on = scheme_color.color_buton_green()
    off = scheme_color.color_buton_red()

    scheme_theme.colorize_status(object.object.edge_1.ID_status_light, param_interface.status_edge_1, on, off)
    scheme_theme.colorize_status(object.object.operator.ID_status_light, param_interface.status_operator, on, off)
    scheme_theme.colorize_status(object.object.ssd.ID_status_light, param_interface.status_ssd, on, off)
    scheme_theme.colorize_status(object.object.control.ID_status_light, param_interface.status_interface, on, off)
    scheme_theme.colorize_status(object.object.edge_1.slam.ID_status_light, param_interface.status_processing, on, off)
    scheme_theme.colorize_status(object.object.edge_1.ai.ID_status_light, param_interface.status_ai, on, off)
    scheme_theme.colorize_status(object.object.capture.ID_status_light, param_interface.status_capture, on, off)
    scheme_theme.colorize_status(object.object.edge_2.ID_status_light, param_interface.status_edge_2, on, off)
    scheme_theme.colorize_status(object.object.train.ID_l1_status_light, param_interface.status_lidar_1, on, off)
    scheme_theme.colorize_status(object.object.train.ID_l2_status_light, param_interface.status_lidar_2, on, off)
    scheme_theme.colorize_status("train_edge_but", param_interface.status_capture, on, off)
    scheme_theme.colorize_status("mongo_server_but", param_interface.status_db, on, off)
def update_add():
    dpg.set_value(object.object.capture.ID_wallet, param_interface.state_edge_1["module_capture"]["add"])
    dpg.set_value(object.object.operator.ID_wallet, param_interface.state_edge_1["cloud_operator"]["add"])
    dpg.set_value(object.object.train.ID_l1_wallet, param_interface.state_capture["lidar_1"]["add"])
    dpg.set_value(object.object.train.ID_l2_wallet, param_interface.state_capture["lidar_2"]["add"])
    dpg.set_value(object.object.edge_1.slam.ID_wallet, param_interface.state_edge_1["component_process"]["add"])
def update_add_combo():
    dpg.configure_item(object.object.capture.ID_wallet, items=param_interface.wallet_add)
    dpg.configure_item(object.object.edge_1.ID_wallet, items=param_interface.wallet_add)
    dpg.configure_item(object.object.edge_2.ID_wallet, items=param_interface.wallet_add)
    dpg.configure_item(object.object.operator.ID_wallet, items=param_interface.wallet_add)
    dpg.configure_item(object.object.train.ID_l1_wallet, items=param_interface.wallet_add)
    dpg.configure_item(object.object.train.ID_l2_wallet, items=param_interface.wallet_add)
    dpg.configure_item(object.object.edge_1.slam.ID_wallet, items=param_interface.wallet_add)

def update_ssd():
    dpg.set_value(object.object.ssd.ID_path, param_interface.path_ssd)
    dpg.set_value(object.object.ssd.ID_memory_total, param_interface.state_control["ssd"]["space_total"])
    dpg.set_value(object.object.ssd.ID_memory_used, param_interface.state_control["ssd"]["space_used"])
    dpg.set_value(object.object.ssd.ID_path_l1, param_interface.state_control["path"]["dir_l1"])
    dpg.set_value(object.object.ssd.ID_path_l2, param_interface.state_control["path"]["dir_l2"])
    dpg.set_value(object.object.ssd.ID_file_name, param_interface.state_control["path"]["file_name"])
def update_train():
    dpg.set_value(object.object.train.ID_l1_ip, param_interface.state_capture["lidar_1"]["ip"])
    dpg.set_value(object.object.train.ID_l1_sock_client_port, param_interface.state_capture["lidar_1"]["port"])
    scheme_theme.colorize_onoff(object.object.train.ID_l1_motor_on, object.object.train.ID_l1_motor_off, param_interface.state_capture["lidar_1"]["running"])

    dpg.set_value(object.object.train.ID_l2_ip, param_interface.state_capture["lidar_2"]["ip"])
    dpg.set_value(object.object.train.ID_l2_sock_client_port, param_interface.state_capture["lidar_2"]["port"])
    scheme_theme.colorize_onoff(object.object.train.ID_l2_motor_on, object.object.train.ID_l2_motor_off, param_interface.state_capture["lidar_2"]["running"])
def update_control():
    dpg.set_value(object.object.control.ID_ip, param_interface.state_control["self"]["ip"])
    dpg.set_value(object.object.control.ID_thread, param_interface.state_control["self"]["nb_thread"])
    dpg.set_value(object.object.control.ID_sock_server_l1_port, param_interface.state_control["self"]["sock_server_l1_port"])
    dpg.set_value(object.object.control.ID_sock_server_l2_port, param_interface.state_control["self"]["sock_server_l2_port"])
    dpg.set_value(object.object.control.ID_temperature, signal.get_temps_core(0))
def update_operator():
    dpg.set_value(object.object.operator.ID_mqtt_broker_port, param_interface.state_edge_1["cloud_operator"]["broker_port"])
    dpg.set_value(object.object.operator.ID_mqtt_topic, param_interface.state_edge_1["cloud_operator"]["mqtt_topic"])
def update_capture():
    dpg.set_value(object.object.capture.ID_ip, param_interface.state_edge_1["module_capture"]["ip"])
    dpg.set_value(object.object.capture.ID_thread, param_interface.state_capture["self"]["nb_thread"])
    dpg.set_value(object.object.capture.ID_http_server_port, int(param_interface.state_capture["self"]["http_server_port"]))
    dpg.set_value(object.object.capture.ID_sock_server_l1_port, param_interface.state_capture["self"]["l1_port"])
    dpg.set_value(object.object.capture.ID_sock_server_l2_port, param_interface.state_capture["self"]["l2_port"])

    devices = io.get_list_device_from_state()
    dpg.configure_item(object.object.capture.ID_device_l1, default_value=param_interface.state_capture["lidar_1"]["device"], items=devices, num_items=len(devices))
    dpg.configure_item(object.object.capture.ID_device_l2, default_value=param_interface.state_capture["lidar_2"]["device"], items=devices, num_items=len(devices))
def update_image():
    # Update image but if format problem close the program
    width, height, channels, data = dpg.load_image(param_interface.path_image)
    if(width == param_interface.image_w and height == param_interface.image_h):
        dpg.set_value("image_in", data)
    else:
        print("[\033[1;31merror\033[0m] Image dimension error [%d/%d] [%d/%d]"% (width, param_interface.image_w, height, param_interface.image_h))
        param_interface.run_loop = False
def update_network():
    dpg.set_value("mongo_ip", param_interface.state_network["mongo"]["ip"])
    dpg.set_value("mongo_port", param_interface.state_network["mongo"]["port"])
    dpg.set_value("mongo_db", param_interface.state_network["mongo"]["database"])
    dpg.set_value("mongo_collection", param_interface.state_network["mongo"]["collection"])
    dpg.set_value("mongo_username", param_interface.state_network["mongo"]["username"])
    dpg.set_value("mongo_password", param_interface.state_network["mongo"]["password"])
    dpg.set_value("mongo_nbdata", param_interface.state_network["mongo"]["nb_data"])

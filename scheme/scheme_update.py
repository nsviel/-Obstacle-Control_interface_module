#---------------------------------------------
from param import param_co
from scheme import scheme_link
from scheme import scheme_plot
from scheme import scheme_color
from scheme import scheme_theme
from src import signal
from src import io

import dearpygui.dearpygui as dpg


def update_scheme():
    scheme_link.update_link_color()
    update_status()
    update_ssd()
    update_train()
    update_controlium()
    update_hubium()
    update_edge()
    update_pywardium()
    update_data()

def update_status():
    dpg.set_value("sncf_status", param_co.status_sncf)
    dpg.set_value("ssd_status", param_co.status_ssd)
    dpg.set_value("co_status", param_co.status_co)
    dpg.set_value("ve_status", param_co.status_ve)
    dpg.set_value("ai_status", param_co.status_ai)
    dpg.set_value("hu_status", param_co.status_hu)
    dpg.set_value("py_status", param_co.status_py)
    dpg.set_value("ed_status", param_co.status_ed)

    on = scheme_color.color_buton_green()
    off = scheme_color.color_buton_red()

    scheme_theme.colorize_status("sncf_status_but", param_co.status_sncf, on, off)
    scheme_theme.colorize_status("ssd_status_but", param_co.status_ssd, on, off)
    scheme_theme.colorize_status("co_status_but", param_co.status_co, on, off)
    scheme_theme.colorize_status("ve_status_but", param_co.status_ve, on, off)
    scheme_theme.colorize_status("ai_status_but", param_co.status_ai, on, off)
    scheme_theme.colorize_status("hu_status_but", param_co.status_hu, on, off)
    scheme_theme.colorize_status("py_status_but", param_co.status_py, on, off)
    scheme_theme.colorize_status("ed_status_but", param_co.status_ed, on, off)
    scheme_theme.colorize_status("l1_status_but", param_co.status_l1, on, off)
    scheme_theme.colorize_status("l2_status_but", param_co.status_l2, on, off)
def update_add():
    dpg.set_value("py_wallet", param_co.state_hu["pywardium"]["add"])
    dpg.set_value("hu_wallet", param_co.state_co["hubium"]["add"])
    dpg.set_value("ed_wallet", param_co.state_hu["edge"]["add"])
    dpg.set_value("sncf_wallet", param_co.state_hu["sncf"]["add"])
def update_add_combo():
    dpg.configure_item("py_wallet", items=param_co.wallet_add)
    dpg.configure_item("hu_wallet", items=param_co.wallet_add)
    dpg.configure_item("ed_wallet", items=param_co.wallet_add)
    dpg.configure_item("sncf_wallet", items=param_co.wallet_add)

def update_ssd():
    dpg.set_value("ssd_path", param_co.path_ssd)
    dpg.set_value("ssd_total", param_co.state_co["ssd"]["space_total"])
    dpg.set_value("ssd_used", param_co.state_co["ssd"]["space_used"])
    dpg.set_value("l1_file_path", param_co.state_co["path"]["dir_l1"])
    dpg.set_value("l2_file_path", param_co.state_co["path"]["dir_l2"])
    dpg.set_value("file_name", param_co.state_co["path"]["file_name"])
def update_train():
    dpg.set_value("l1_ip", param_co.state_py["lidar_1"]["ip"])
    dpg.set_value("l1_port", param_co.state_py["lidar_1"]["port"])
    scheme_theme.colorize_onoff("l1_on", "l1_off", param_co.state_py["lidar_1"]["running"])

    dpg.set_value("l2_ip", param_co.state_py["lidar_2"]["ip"])
    dpg.set_value("l2_port", param_co.state_py["lidar_2"]["port"])
    scheme_theme.colorize_onoff("l2_on", "l2_off", param_co.state_py["lidar_2"]["running"])

    dpg.set_value("geo_country", param_co.state_py["geolocalization"]["country"])
def update_controlium():
    dpg.set_value("co_ip", param_co.state_co["self"]["ip"])
    dpg.set_value("co_thread", param_co.state_co["self"]["nb_thread"])
    dpg.set_value("co_sock_server_l1_port", param_co.state_co["self"]["sock_server_l1_port"])
    dpg.set_value("co_sock_server_l2_port", param_co.state_co["self"]["sock_server_l2_port"])
    dpg.set_value("co_temp", signal.get_temps_core(0))
def update_hubium():
    dpg.set_value("hu_ip", param_co.state_co["hubium"]["ip"])
    dpg.set_value("hu_thread", param_co.state_hu["self"]["nb_thread"])

    dpg.set_value("hu_country", param_co.state_hu["self"]["country"])
    dpg.set_value("hu_edge_id", param_co.state_hu["self"]["edge_id"])
    dpg.set_value("ve_sock_server_port", param_co.state_hu["velodium"]["sock_server_port"])
    dpg.set_value("ve_http_server_port", param_co.state_hu["velodium"]["http_server_port"])
    dpg.set_value("ai_http_server_port", param_co.state_hu["ai"]["http_server_port"])
    dpg.set_value("hu_sock_server_l1_port", param_co.state_hu["self"]["sock_server_l1_port"])
    dpg.set_value("hu_sock_server_l2_port", param_co.state_hu["self"]["sock_server_l2_port"])
    dpg.set_value("hu_http_server_port", param_co.state_hu["self"]["http_server_port"])
    dpg.set_value("sncf_broker_port", param_co.state_hu["sncf"]["broker_port"])
    dpg.set_value("sncf_mqtt_topic", param_co.state_hu["sncf"]["mqtt_topic"])
def update_edge():
    dpg.set_value("ed_ip", param_co.state_hu["edge"]["ip"])
    #dpg.set_value("ed_country", param_co.state_hu["edge"]["country"])
    #dpg.set_value("ed_edge_id", param_co.state_hu["edge"]["edge_id"])
    dpg.set_value("ed_sock_server_port", param_co.state_hu["self"]["sock_server_l1_port"])
    dpg.set_value("ed_http_server_port", param_co.state_hu["self"]["http_server_port"])
def update_pywardium():
    dpg.set_value("py_ip", param_co.state_hu["pywardium"]["ip"])
    dpg.set_value("py_thread", param_co.state_py["self"]["nb_thread"])
    dpg.set_value("py_http_server_port", int(param_co.state_py["self"]["http_server_port"]))
    dpg.set_value("py_l1_port", param_co.state_py["self"]["l1_port"])
    dpg.set_value("py_l2_port", param_co.state_py["self"]["l2_port"])

    devices = io.get_list_device_from_state()
    dpg.configure_item("py_l1_device", default_value=param_co.state_py["lidar_1"]["device"], items=devices, num_items=len(devices))
    dpg.configure_item("py_l2_device", default_value=param_co.state_py["lidar_2"]["device"], items=devices, num_items=len(devices))
def update_data():
    dpg.set_value("nb_frame", param_co.state_hu["data"]["nb_frame"])
    dpg.set_value("nb_prediction", param_co.state_hu["data"]["nb_prediction"])
def update_image():
    width, height, channels, data = dpg.load_image(param_co.path_image)
    dpg.set_value("image_in", data)

def update_node_pos_dev():
    gui_width = param_co.state_co["gui"]["width"]
    gui_height = param_co.state_co["gui"]["height"]
    coord_controlium = [375, 550]
    coord_pywardium = [350, 10]
    coord_hubium = [835, 375]
    coord_train = [10, 10]
    coord_edge = [1200, 525]
    coord_velodium = [1200, 5]
    coord_ai = [1200, 215]
    coord_sncf = [1200, 380]
    coord_valeo = [1200, 745]
    coord_ssd = [10, 520]
    coord_data = [755, 10]
    coord_network = [10, 400]

    dpg.set_item_pos("node_co", coord_controlium)
    dpg.set_item_pos("node_hu", coord_hubium)
    dpg.set_item_pos("node_py", coord_pywardium)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_ed", coord_edge)
    dpg.set_item_pos("node_ve", coord_velodium)
    dpg.set_item_pos("node_ai", coord_ai)
    dpg.set_item_pos("node_sncf", coord_sncf)
    dpg.set_item_pos("node_valeo", coord_valeo)
    dpg.set_item_pos("node_ssd", coord_ssd)
    dpg.set_item_pos("node_data", coord_data)
    dpg.set_item_pos("window_perf", coord_network)

    update_fullscreen(False)
    dpg.set_viewport_width(gui_width)
    dpg.set_viewport_height(gui_height)
    scheme_theme.scheme_theme_dev()
def update_node_pos_demo_minimized():
    gui_width = 1100
    gui_height = 650
    coord_controlium = [250, 440]
    coord_pywardium = [250, 10]
    coord_hubium = [575, 325]
    coord_train = [10, 100]
    coord_velodium = [900, 265]
    coord_ai = [900, 450]
    coord_sncf = [900, 125]
    coord_ssd = [10, 440]
    coord_data = [500, 10]
    coord_legend = [850, 10]
    coord_network = [10, 10]

    dpg.set_item_pos("node_co", coord_controlium)
    dpg.set_item_pos("node_hu", coord_hubium)
    dpg.set_item_pos("node_py", coord_pywardium)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_ve", coord_velodium)
    dpg.set_item_pos("node_ai", coord_ai)
    dpg.set_item_pos("node_sncf", coord_sncf)
    dpg.set_item_pos("node_ssd", coord_ssd)
    dpg.set_item_pos("node_data", coord_data)
    dpg.set_item_pos("node_legend", coord_legend)
    dpg.set_item_pos("window_perf", coord_network)

    update_fullscreen(False)
    dpg.set_viewport_width(gui_width)
    dpg.set_viewport_height(gui_height)
    scheme_theme.scheme_theme_demo()
def update_node_pos_demo_fullscreen():
    coord_controlium = [500, 700]
    coord_pywardium = [500, 300]
    coord_hubium = [1055, 500]
    coord_train = [50, 300]
    coord_velodium = [1600, 350]
    coord_ai = [1600, 700]
    coord_sncf = [1600, 100]
    coord_ssd = [50, 700]
    coord_data = [1000, 10]
    coord_legend = [10, 10]
    coord_network = [400, 10]

    dpg.set_item_pos("node_co", coord_controlium)
    dpg.set_item_pos("node_hu", coord_hubium)
    dpg.set_item_pos("node_py", coord_pywardium)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_ve", coord_velodium)
    dpg.set_item_pos("node_ai", coord_ai)
    dpg.set_item_pos("node_sncf", coord_sncf)
    dpg.set_item_pos("node_ssd", coord_ssd)
    dpg.set_item_pos("node_data", coord_data)
    dpg.set_item_pos("node_legend", coord_legend)
    dpg.set_item_pos("window_perf", coord_network)

    update_fullscreen(True)
    scheme_theme.scheme_theme_demo()
def update_fullscreen(value):
    if(param_co.gui_fullscreen == False and value == True):
        dpg.toggle_viewport_fullscreen()
        dpg.bind_item_font("window", param_co.gui_font_big)
        dpg.set_item_width("py_wallet", 175)
        dpg.set_item_width("hu_wallet", 175)
        dpg.set_item_width("ve_wallet", 175)
        dpg.set_item_width("ai_wallet", 175)
        dpg.set_item_width("sncf_wallet", 175)
        dpg.set_item_width("ai_lidar_height", 150)
        dpg.set_item_width("ai_threshold", 150)
        dpg.set_item_width("hu_sock_client_l1_source", 120)
        dpg.set_item_width("legend_train", 30)
        dpg.set_item_width("legend_edge", 30)
        dpg.set_item_width("legend_cloud", 30)
        dpg.set_item_width("legend_control", 30)
        dpg.set_item_width("l1_speed", 125)
        param_co.gui_fullscreen = True
    elif(param_co.gui_fullscreen == True and value == False):
        dpg.toggle_viewport_fullscreen()
        dpg.bind_item_font("window", param_co.gui_font_def)
        dpg.set_item_width("py_wallet", 120)
        dpg.set_item_width("hu_wallet", 120)
        dpg.set_item_width("ve_wallet", 120)
        dpg.set_item_width("ai_wallet", 120)
        dpg.set_item_width("sncf_wallet", 120)
        dpg.set_item_width("ai_lidar_height", 100)
        dpg.set_item_width("ai_threshold", 100)
        dpg.set_item_width("hu_sock_client_l1_source", 80)
        dpg.set_item_width("legend_train", 15)
        dpg.set_item_width("legend_edge", 15)
        dpg.set_item_width("legend_cloud", 15)
        dpg.set_item_width("legend_control", 15)
        dpg.set_item_width("l1_speed", 75)
        param_co.gui_fullscreen = False

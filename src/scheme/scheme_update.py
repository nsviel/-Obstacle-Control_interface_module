#---------------------------------------------
from src.param import param_interface
from src.scheme import scheme_link
from src.scheme import scheme_plot
from src.scheme import scheme_color
from src.scheme import scheme_theme
from src.misc import signal
from src.misc import io
from src import loop

import dearpygui.dearpygui as dpg


def update_scheme():
    scheme_link.update_link_color()
    update_status()
    update_ssd()
    update_train()
    update_module_interface()
    update_component_process()
    update_module_edge()
    update_edge_next()
    update_module_capture()
    update_data()
    update_network()

def update_status():
    dpg.set_value("trainope_status", param_interface.status_operator)
    dpg.set_value("ssd_status", param_interface.status_ssd)
    dpg.set_value("interface_status", param_interface.status_co)
    dpg.set_value("processing_status", param_interface.status_ve)
    dpg.set_value("ai_status", param_interface.status_ai)
    dpg.set_value("edge_status", param_interface.status_hu)
    dpg.set_value("capture_status", param_interface.status_py)
    dpg.set_value("edgenext_status", param_interface.status_ed)

    on = scheme_color.color_buton_green()
    off = scheme_color.color_buton_red()

    scheme_theme.colorize_status("trainope_status_but", param_interface.status_operator, on, off)
    scheme_theme.colorize_status("ssd_status_but", param_interface.status_ssd, on, off)
    scheme_theme.colorize_status("interface_status_but", param_interface.status_co, on, off)
    scheme_theme.colorize_status("processing_status_but", param_interface.status_ve, on, off)
    scheme_theme.colorize_status("ai_status_but", param_interface.status_ai, on, off)
    scheme_theme.colorize_status("edge_status_but", param_interface.status_hu, on, off)
    scheme_theme.colorize_status("capture_status_but", param_interface.status_py, on, off)
    scheme_theme.colorize_status("edgenext_status_but", param_interface.status_ed, on, off)
    scheme_theme.colorize_status("l1_status_but", param_interface.status_l1, on, off)
    scheme_theme.colorize_status("l2_status_but", param_interface.status_l2, on, off)
    scheme_theme.colorize_status("train_edge_but", param_interface.status_py, on, off)
    scheme_theme.colorize_status("mongo_server_but", param_interface.status_db, on, off)
def update_add():
    dpg.set_value("capture_wallet", param_interface.state_edge["module_capture"]["add"])
    dpg.set_value("edge_wallet", param_interface.state_interface["edge"]["add"])
    dpg.set_value("edgenext_wallet", param_interface.state_edge["edge_next"]["add"])
    dpg.set_value("trainope_wallet", param_interface.state_edge["train_operator"]["add"])
    dpg.set_value("l1_wallet", param_interface.state_capture["lidar_1"]["add"])
    dpg.set_value("l2_wallet", param_interface.state_capture["lidar_2"]["add"])
    dpg.set_value("processing_wallet", param_interface.state_edge["component_process"]["add"])
def update_add_combo():
    dpg.configure_item("capture_wallet", items=param_interface.wallet_add)
    dpg.configure_item("edge_wallet", items=param_interface.wallet_add)
    dpg.configure_item("edgenext_wallet", items=param_interface.wallet_add)
    dpg.configure_item("trainope_wallet", items=param_interface.wallet_add)
    dpg.configure_item("l1_wallet", items=param_interface.wallet_add)
    dpg.configure_item("l2_wallet", items=param_interface.wallet_add)
    dpg.configure_item("processing_wallet", items=param_interface.wallet_add)

def update_ssd():
    dpg.set_value("ssd_path", param_interface.path_ssd)
    dpg.set_value("ssd_total", param_interface.state_interface["ssd"]["space_total"])
    dpg.set_value("ssd_used", param_interface.state_interface["ssd"]["space_used"])
    dpg.set_value("l1_file_path", param_interface.state_interface["path"]["dir_l1"])
    dpg.set_value("l2_file_path", param_interface.state_interface["path"]["dir_l2"])
    dpg.set_value("file_name", param_interface.state_interface["path"]["file_name"])
def update_train():
    dpg.set_value("l1_ip", param_interface.state_capture["lidar_1"]["ip"])
    dpg.set_value("l1_port", param_interface.state_capture["lidar_1"]["port"])
    scheme_theme.colorize_onoff("l1_on", "l1_off", param_interface.state_capture["lidar_1"]["running"])

    dpg.set_value("l2_ip", param_interface.state_capture["lidar_2"]["ip"])
    dpg.set_value("l2_port", param_interface.state_capture["lidar_2"]["port"])
    scheme_theme.colorize_onoff("l2_on", "l2_off", param_interface.state_capture["lidar_2"]["running"])

    dpg.set_value("geo_country", param_interface.state_capture["geolocalization"]["country"])
def update_module_interface():
    dpg.set_value("interface_ip", param_interface.state_interface["self"]["ip"])
    dpg.set_value("interface_thread", param_interface.state_interface["self"]["nb_thread"])
    dpg.set_value("interface_sock_server_l1_port", param_interface.state_interface["self"]["sock_server_l1_port"])
    dpg.set_value("interface_sock_server_l2_port", param_interface.state_interface["self"]["sock_server_l2_port"])
    dpg.set_value("interface_temp", signal.get_temps_core(0))
def update_module_edge():
    dpg.set_value("edge_ip", param_interface.state_edge["self"]["ip"])
    dpg.set_value("edge_thread", param_interface.state_edge["self"]["nb_thread"])

    dpg.set_value("edge_country", param_interface.state_edge["self"]["country"])
    dpg.set_value("edge_edge_id", param_interface.state_edge["self"]["edge_id"])
    dpg.set_value("processing_sock_server_port", param_interface.state_edge["component_process"]["sock_server_port"])
    dpg.set_value("processing_http_server_port", param_interface.state_edge["component_process"]["http_server_port"])
    dpg.set_value("ai_http_server_port", param_interface.state_edge["component_ai"]["http_server_port"])
    dpg.set_value("edge_sock_server_l1_port", param_interface.state_edge["self"]["sock_server_l1_port"])
    dpg.set_value("edge_sock_server_l2_port", param_interface.state_edge["self"]["sock_server_l2_port"])
    dpg.set_value("edge_http_server_port", param_interface.state_edge["self"]["http_server_port"])
    dpg.set_value("trainope_broker_port", param_interface.state_edge["train_operator"]["broker_port"])
    dpg.set_value("trainope_mqtt_topic", param_interface.state_edge["train_operator"]["mqtt_topic"])

    if(param_interface.state_edge["self"]["lidar_main"] == "lidar_1"):
        s1 = "lidar_1"
        s2 = "lidar_2"
    elif(param_interface.state_edge["self"]["lidar_main"] == "lidar_2"):
        s1 = "lidar_2"
        s2 = "lidar_1"
    dpg.set_value("edge_sock_client_l1_combo_lidar_main", s1)
    dpg.set_value("edge_sock_client_l2_source", s2)
def update_edge_next():
    dpg.set_value("edgenext_ip", param_interface.state_edge["edge_next"]["ip"])
    #dpg.set_value("edgenext_country", param_interface.state_edge["edge"]["country"])
    #dpg.set_value("edgenext_edge_id", param_interface.state_edge["edge"]["edge_id"])
    dpg.set_value("edgenext_sock_server_port", param_interface.state_edge["self"]["sock_server_l1_port"])
    dpg.set_value("edgenext_http_server_port", param_interface.state_edge["self"]["http_server_port"])
def update_component_process():
    dpg.set_value("processing_ip", param_interface.state_edge["component_process"]["ip"])
def update_module_capture():
    dpg.set_value("capture_ip", param_interface.state_edge["module_capture"]["ip"])
    dpg.set_value("capture_thread", param_interface.state_capture["self"]["nb_thread"])
    dpg.set_value("capture_http_server_port", int(param_interface.state_capture["self"]["http_server_port"]))
    dpg.set_value("capture_l1_port", param_interface.state_capture["self"]["l1_port"])
    dpg.set_value("capture_l2_port", param_interface.state_capture["self"]["l2_port"])

    devices = io.get_list_device_from_state()
    dpg.configure_item("capture_l1_device", default_value=param_interface.state_capture["lidar_1"]["device"], items=devices, num_items=len(devices))
    dpg.configure_item("capture_l2_device", default_value=param_interface.state_capture["lidar_2"]["device"], items=devices, num_items=len(devices))
def update_data():
    dpg.set_value("nb_frame", param_interface.state_edge["data"]["nb_frame"])
    dpg.set_value("nb_prediction", param_interface.state_edge["data"]["nb_prediction"])
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

def update_node_pos_dev():
    gui_width = param_interface.state_interface["gui"]["width"]
    gui_height = param_interface.state_interface["gui"]["height"]
    coord_module_interface = [1100, 600]
    coord_module_capture = [250, 10]
    coord_module_edge = [725, 400]
    coord_train = [10, 10]
    coord_edge_next = [1150, 215]
    coord_component_process = [400, 510]
    coord_ai = [400, 745]
    coord_trainope = [1150, 50]
    coord_cloud_car = [1150, 450]
    coord_ssd = [1325, 600]
    coord_data = [650, 10]
    coord_network = [10, 510]

    dpg.set_item_pos("node_co", coord_module_interface)
    dpg.set_item_pos("node_hu", coord_module_edge)
    dpg.set_item_pos("node_py", coord_module_capture)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_ed", coord_edge_next)
    dpg.set_item_pos("node_ve", coord_component_process)
    dpg.set_item_pos("node_ai", coord_ai)
    dpg.set_item_pos("node_operator", coord_trainope)
    dpg.set_item_pos("node_cloud_car", coord_cloud_car)
    dpg.set_item_pos("node_ssd", coord_ssd)
    dpg.set_item_pos("node_data", coord_data)
    dpg.set_item_pos("node_network", coord_network)

    dpg.set_viewport_width(gui_width)
    dpg.set_viewport_height(gui_height)
    scheme_theme.scheme_theme_dev()
def update_node_pos_demo_minimized():
    gui_width = 1350
    gui_height = 750
    coord_module_interface = [1175, 325]
    coord_module_capture = [290, 100]
    coord_module_edge = [775, 425]
    coord_train = [25, 100]
    coord_component_process = [850, 350]
    coord_ai = [850, 550]
    coord_trainope = [1110, 250]
    coord_ssd = [1400, 325]
    coord_data = [700, 100]
    coord_legend = [1110, 10]
    coord_network = [75, 400]
    coord_block_train = [10, 10]
    coord_block_edge = [675, 10]
    coord_block_cloud = [1075, 10]

    dpg.set_item_pos("node_block_train", coord_block_train)
    dpg.set_item_pos("node_block_edge", coord_block_edge)
    dpg.set_item_pos("node_block_cloud", coord_block_cloud)

    dpg.set_item_pos("node_co", coord_module_interface)
    dpg.set_item_pos("node_hu", coord_module_edge)
    dpg.set_item_pos("node_py", coord_module_capture)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_ve", coord_component_process)
    dpg.set_item_pos("node_ai", coord_ai)
    dpg.set_item_pos("node_operator", coord_trainope)
    dpg.set_item_pos("node_ssd", coord_ssd)
    dpg.set_item_pos("node_data", coord_data)
    dpg.set_item_pos("node_network", coord_network)

    dpg.set_viewport_width(gui_width)
    dpg.set_viewport_height(gui_height)
    scheme_theme.scheme_theme_demo()
def update_node_pos_demo_fullscreen():
    gui_width = 1875
    gui_height = 1040
    coord_module_interface = [1175, 325]
    coord_module_capture = [290, 150]
    coord_module_edge = [875, 525]
    coord_train = [50, 150]
    coord_component_process = [850, 350]
    coord_ai = [850, 550]
    coord_trainope = [1485, 250]
    coord_ssd = [1400, 325]
    coord_data = [800, 225]
    coord_legend = [1110, 10]
    coord_network = [150, 600]
    coord_block_train = [35, 50]
    coord_block_edge = [775, 125]
    coord_block_cloud = [1450, 50]

    dpg.set_item_pos("node_block_train", coord_block_train)
    dpg.set_item_pos("node_block_edge", coord_block_edge)
    dpg.set_item_pos("node_block_cloud", coord_block_cloud)

    dpg.set_item_pos("node_co", coord_module_interface)
    dpg.set_item_pos("node_hu", coord_module_edge)
    dpg.set_item_pos("node_py", coord_module_capture)
    dpg.set_item_pos("node_train", coord_train)
    dpg.set_item_pos("node_ve", coord_component_process)
    dpg.set_item_pos("node_ai", coord_ai)
    dpg.set_item_pos("node_operator", coord_trainope)
    dpg.set_item_pos("node_ssd", coord_ssd)
    dpg.set_item_pos("node_data", coord_data)
    dpg.set_item_pos("node_network", coord_network)

    dpg.set_viewport_width(gui_width)
    dpg.set_viewport_height(gui_height)
    scheme_theme.scheme_theme_demo()
def update_fullscreen(value):
    if(param_interface.gui_fullscreen == False and value == True):
        dpg.toggle_viewport_fullscreen()
        dpg.bind_item_font("window", param_interface.gui_font_big)
        dpg.set_item_width("capture_wallet", 175)
        dpg.set_item_width("edge_wallet", 175)
        dpg.set_item_width("processing_wallet", 175)
        dpg.set_item_width("ai_wallet", 175)
        dpg.set_item_width("trainope_wallet", 175)
        dpg.set_item_width("ai_lidar_height", 150)
        dpg.set_item_width("ai_threshold", 150)
        dpg.set_item_width("edge_sock_client_l1_combo_lidar_main", 120)
        dpg.set_item_width("legend_train", 30)
        dpg.set_item_width("legend_edge", 30)
        dpg.set_item_width("legend_cloud", 30)
        dpg.set_item_width("legend_control", 30)
        dpg.set_item_width("l1_speed", 125)
        param_interface.gui_fullscreen = True
    elif(param_interface.gui_fullscreen == True and value == False):
        dpg.toggle_viewport_fullscreen()
        dpg.bind_item_font("window", param_interface.gui_font_def)
        dpg.set_item_width("capture_wallet", 120)
        dpg.set_item_width("edge_wallet", 120)
        dpg.set_item_width("processing_wallet", 120)
        dpg.set_item_width("ai_wallet", 120)
        dpg.set_item_width("trainope_wallet", 120)
        dpg.set_item_width("ai_lidar_height", 100)
        dpg.set_item_width("ai_threshold", 100)
        dpg.set_item_width("edge_sock_client_l1_combo_lidar_main", 80)
        dpg.set_item_width("legend_train", 15)
        dpg.set_item_width("legend_edge", 15)
        dpg.set_item_width("legend_cloud", 15)
        dpg.set_item_width("legend_control", 15)
        dpg.set_item_width("l1_speed", 75)
        param_interface.gui_fullscreen = False

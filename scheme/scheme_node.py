#---------------------------------------------
from param import param_co
from scheme import scheme_function
from scheme import scheme_connection
from scheme import scheme_callback
from scheme import scheme_command

import dearpygui.dearpygui as dpg


def node_controlium():
    with dpg.node(label="Controlium", tag="node_co"):
        scheme_function.add_status_i("co_input", "co_status_but", "co_status")
        scheme_function.add_ip("co_ip")
        scheme_function.add_nb_thread("co_thread", "co_thread_visible")
        scheme_function.add_temperature("co_temp", "co_temp_visibile")

        scheme_function.add_false_alarm()
        scheme_function.add_choice_edge("combo_edge")

        scheme_connection.add_http_client_o("co_http_client")

        scheme_connection.add_sock_server_o("co_sock_server_l1")
        scheme_function.add_port_co("co_sock_server_l1_port", "co_port_l1_visible")

        scheme_connection.add_sock_server_o("co_sock_server_l2")
        scheme_function.add_port_co("co_sock_server_l2_port", "co_port_l2_visible")

def node_pywardium():
    with dpg.node(label="Pywardium", tag="node_py"):
        scheme_function.add_status_i("py_input", "py_status_but", "py_status")
        scheme_function.add_ip_wallet("py_wallet", "py_ip", "-")
        scheme_function.add_nb_thread("py_thread", "py_thread_visible")

        scheme_function.add_port_fixe_i("py_l1_in", "py_l1_port", "py_l1_port_visible")
        scheme_connection.add_sock_client_o_("py_l1_out")
        scheme_function.add_port_fixe_i("py_l2_in", "py_l2_port", "py_l2_port_visible")
        scheme_connection.add_sock_client_o_("py_l2_out")

        scheme_function.add_lidar_device("py_l1_device", "py_l2_device", "py_l2_dev_visible")

        scheme_connection.add_http_server_o("py_http_server")
        scheme_function.add_port_fixe("py_http_server_port", "py_http_port_visible")

def node_hubium():
    with dpg.node(label="Hubium", tag="node_hu"):
        scheme_function.add_status("hu_status_but", "hu_status")
        scheme_function.add_ip_wallet("hu_wallet", "hu_ip", param_co.state_co["hubium"]["add"])
        scheme_function.add_nb_thread("hu_thread", "hu_thread_visible")

        scheme_function.add_edge_id("hu_edge_id", "hu_edge_id_visible")
        scheme_function.add_country("hu_country")
        scheme_function.add_mqtt("hu_mqtt_client", "hu_mqtt_client_name", "hu_mqtt_visible")

        scheme_connection.add_sock_server_io("hu_sock_server_l1_i", "hu_sock_server_l1_o")
        scheme_function.add_port_hu("hu_sock_server_l1_port", "hu_port_l1_visible")
        scheme_connection.add_sock_server_i("hu_sock_server_l2_i")
        scheme_function.add_port_hu("hu_sock_server_l2_port", "hu_port_l2_visible")

        scheme_connection.add_sock_client_source_io("hu_sock_client_l1_i", "hu_sock_client_l1_o", "hu_sock_client_l1_source")
        scheme_connection.add_sock_client_source_i("hu_sock_client_l2_i", "hu_sock_client_l2_source")

        scheme_connection.add_http_client_io("hu_http_client_i", "hu_http_client_o")
        scheme_connection.add_http_server_io("hu_http_server_i", "hu_http_server_o")
        scheme_function.add_port_fixe("hu_http_server_port", "hu_http_port_visible")

def node_train():
    with dpg.node(label="Train", tag="node_train"):
        scheme_function.add_geolocalization("geo_status", "geo_country")

        scheme_function.add_lidar_status("Lidar 1", "l1_status", "l1_activated", "l1_status_but")
        scheme_function.add_l1_motor("l1_on", "l1_off")
        scheme_function.add_lidar_param("l1_ip", "l1_port", "l1_params_visible")
        scheme_function.add_lidar_speed("l1_speed", "l1_speed_visible")
        scheme_function.add_lidar_stat("l1_packet", "l1_bdw_val", "l1_bdw_range", "l1_perf_visible")

        scheme_function.add_lidar_status("Lidar 2", "l2_status", "l2_activated", "l2_status_but")
        scheme_function.add_l2_motor("l2_on", "l2_off", "l2_motor_visible")
        scheme_function.add_lidar_param("l2_ip", "l2_port", "l2_params_visible")
        scheme_function.add_lidar_speed("l2_speed", "l2_speed_visible")
        scheme_function.add_lidar_stat("l2_packet", "l2_bdw_val", "l2_bdw_range", "l2_perf_visible")

        #scheme_function.add_variable("Time:", "capture_time")

def node_edge():
    with dpg.node(label="Edge", tag="node_ed"):
        scheme_function.add_status("ed_status_but", "ed_status")
        scheme_function.add_ip_wallet("ed_wallet", "ed_ip", param_co.state_hu["edge"]["add"])
        #scheme_function.add_edge_id("ed_edge_id")
        #scheme_function.add_country("ed_country")

        scheme_connection.add_sock_client_i("ed_sock_client")

        scheme_connection.add_sock_server_i("ed_sock_server")
        scheme_function.add_port_fixe("ed_sock_server_port", "ed_sock_port_visible")

        scheme_connection.add_http_client_i("ed_http_client")
        scheme_connection.add_http_server_i("ed_http_server")
        scheme_function.add_port_fixe("ed_http_server_port", "ed_http_port_visible")

def node_ve():
    with dpg.node(label="Velodium", tag="node_ve"):
        scheme_function.add_status("ve_status_but", "ve_status")
        scheme_function.add_ip_wallet("ve_wallet", "ve_ip", "localhost")
        scheme_function.add_velo_option("ve_opt_slam", "ve_opt_view")
        scheme_connection.add_sock_server_i("ve_sock_server")
        scheme_function.add_port_fixe("ve_sock_server_port", "ve_sock_port_visible")
        scheme_connection.add_http_server_i("ve_http_server")
        scheme_function.add_port_fixe("ve_http_server_port", "ve_http_port_visible")

def node_ai():
    with dpg.node(label="AI", tag="node_ai"):
        scheme_function.add_status("ai_status_but", "ai_status")
        scheme_function.add_ip_wallet("ai_wallet", "ai_ip", "localhost")
        scheme_function.add_ai_param_height("ai_lidar_height")
        scheme_function.add_ai_param_thres("ai_threshold")
        scheme_connection.add_http_server_i("ai_http_server")
        scheme_function.add_port_fixe("ai_http_server_port", "ai_http_port_visible")

def node_sncf():
    with dpg.node(label="SNCF", tag="node_sncf"):
        scheme_function.add_status("sncf_status_but", "sncf_status")
        scheme_function.add_ip_wallet("sncf_wallet", "sncf_ip", param_co.state_hu["sncf"]["add"])
        scheme_function.add_input("MQTT", "sncf_mqtt_broker")
        scheme_function.add_port_sncf("sncf_broker_port", "ai_sncf_port_visible")
        scheme_function.add_mqtt_topic("sncf_mqtt_topic", "sncf_mqtt_topic_visible")

def node_valeo():
    with dpg.node(label="Valeo", tag="node_valeo"):
        scheme_function.add_ip("va_ip")
        scheme_connection.add_http_client_i("va_http_client")

def node_ssd():
    with dpg.node(label="SSD", tag="node_ssd"):
        scheme_function.add_status_o("ssd_input", "ssd_status_but", "ssd_status")
        scheme_function.add_ssd_active("ssd_active")
        scheme_function.add_ssd_param("ssd_path", "file_name", "ssd_path_add", "ssd_used", "ssd_total", "ssd_param_visible")
        scheme_function.add_file_info("Lidar 1", "l1_file_path", "l1_file_size", "ssd_l1_visible")
        scheme_function.add_file_info("Lidar 2", "l2_file_path", "l2_file_size", "ssd_l2_visible")

def node_data():
    with dpg.node(label="Data", tag="node_data"):
        scheme_function.add_image("image_in")
        scheme_function.add_plot("lidar 1", "l1_yaxis", "l1_plot", "l1_plot_visible")
        scheme_function.add_plot("lidar 2", "l2_yaxis", "l2_plot", "l2_plot_visible")
        scheme_function.add_variable_simple("Frame:", "nb_frame")
        scheme_function.add_variable_simple("Prediction:", "nb_prediction")

def node_stats():
    with dpg.node(label="", tag="node_stat_co", pos=[575, 650]):
        scheme_function.add_variable_simple("Speed:", "co_speed")
        scheme_function.add_variable_simple("Latency:", "co_latency")
        scheme_function.add_variable_simple("Bandwidth:", "co_bw")

    with dpg.node(label="", tag="node_stat_py", pos=[650, 50]):
        scheme_function.add_variable_simple("Speed:", "py_speed")
        scheme_function.add_variable_simple("Bandwidth:", "py_bw")

    with dpg.node(label="", tag="node_stat_ed", pos=[1100, 400]):
        scheme_function.add_variable_simple("Speed:", "ed_speed")
        scheme_function.add_variable_simple("Bandwidth:", "ed_bw")

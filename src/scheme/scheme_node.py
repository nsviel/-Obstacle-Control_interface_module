#---------------------------------------------
from src.param import param_co
from src.scheme import scheme_function
from src.scheme import scheme_connection
from src.scheme import scheme_callback
from src.scheme import scheme_com
from src.scheme import scheme_com_mongo

import dearpygui.dearpygui as dpg


def create_node():
    node_block_train()
    node_block_edge()
    node_block_cloud()

    node_controlium()
    node_pywardium()
    node_hubium()
    node_train()
    node_edge()
    node_ve()
    node_ai()
    node_sncf()
    node_valeo()
    node_ssd()
    node_data()
    node_network()

def node_controlium():
    with dpg.node(label="System control interface", tag="node_co"):
        scheme_function.add_status_o("co_input", "co_status_but", "co_status")
        scheme_function.add_ip("co_ip")
        scheme_function.add_nb_thread("co_thread", "co_thread_visible")
        scheme_function.add_temperature("co_temp", "co_temp_visibile")

        scheme_function.add_choice_edge("combo_edge")

        scheme_connection.add_http_client_i("co_http_client")

        scheme_connection.add_sock_server_i("co_sock_server_l1")
        scheme_function.add_port_co("co_sock_server_l1_port", "co_port_l1_visible")

        scheme_connection.add_sock_server_i("co_sock_server_l2")
        scheme_function.add_port_co("co_sock_server_l2_port", "co_port_l2_visible")

def node_pywardium():
    with dpg.node(label="Train module", tag="node_py"):
        scheme_function.add_image("icon_computer", "icon_computer_visible")

        scheme_function.add_status_i("py_input", "py_status_but", "py_status")
        scheme_function.add_ip_wallet("py_wallet", "py_ip", "-", "py_ip_visible")
        scheme_function.add_nb_thread("py_thread", "py_thread_visible")

        #scheme_function.add_iperf_py()

        scheme_function.add_port_fixe_i("py_l1_in", "py_l1_port", "py_l1_port_visible")
        scheme_connection.add_sock_client_o_("py_l1_out")
        scheme_function.add_port_fixe_i("py_l2_in", "py_l2_port", "py_l2_port_visible")
        scheme_connection.add_sock_client_o_("py_l2_out")

        scheme_function.add_lidar_device("py_l1_device", "py_l2_device", "py_lidar_dev_visible")

        scheme_connection.add_http_server_o("py_http_server")
        scheme_function.add_port_fixe("py_http_server_port", "py_http_port_visible")

def node_hubium():
    with dpg.node(label="Edge AI module", tag="node_hu"):
        scheme_function.add_status("hu_status_but", "hu_status")
        scheme_function.add_ip_wallet("hu_wallet", "hu_ip", param_co.state_co["hubium"]["add"], "hu_ip_visible")
        scheme_function.add_nb_thread("hu_thread", "hu_thread_visible")

        scheme_function.add_edge_id("hu_edge_id", "hu_edge_id_visible")
        scheme_function.add_country("hu_country")
        scheme_function.add_mqtt("hu_mqtt_client", "hu_mqtt_client_name", "hu_mqtt_visible")
        scheme_function.add_false_alarm()

        scheme_connection.add_sock_server_io("hu_sock_server_l1_i", "hu_sock_server_l1_o")
        scheme_function.add_port_hu("hu_sock_server_l1_port", "hu_port_l1_visible")
        scheme_connection.add_sock_server_i("hu_sock_server_l2_i")
        scheme_function.add_port_hu("hu_sock_server_l2_port", "hu_port_l2_visible")

        scheme_connection.add_sock_client_source_io("hu_sock_client_l1_i", "hu_sock_client_l1_o", "hu_sock_client_l1_combo_lidar_main", "hu_src_1", "hu_src_2")
        scheme_connection.add_sock_client_source_o("hu_sock_client_l2_o", "hu_sock_client_l2_source")

        scheme_connection.add_http_client_io("hu_http_client_i", "hu_http_client_o")
        scheme_connection.add_http_server_o("hu_http_server_o")
        scheme_function.add_port_fixe("hu_http_server_port", "hu_http_port_visible")

def node_train():
    with dpg.node(label="LiDAR", tag="node_train"):
        scheme_function.add_image("icon_lidar", "icon_lidar_visible")
        scheme_function.add_geolocalization("geo_status", "geo_country")

        scheme_function.line_tagged("l1_line_visible")
        scheme_function.add_lidar_status("Lidar 1", "l1_status", "l1_activated", "l1_status_but")
        scheme_function.add_l1_motor("l1_on", "l1_off", "l1_motor_visible")
        scheme_function.add_lidar_add("l1_wallet", "l1_ip", "l1_params_visible")
        scheme_function.add_port_lidar("l1_port", "l1_port_visible")
        scheme_function.add_l1_speed("l1_speed", "l1_speed_visible")
        scheme_function.add_lidar_stat("l1_packet", "l1_tgp_val", "l1_tgp_range", "l1_perf_visible")

        scheme_function.line_tagged("l2_line_visible")
        scheme_function.add_lidar_status("Lidar 2", "l2_status", "l2_activated", "l2_status_but")
        scheme_function.add_l2_motor("l2_on", "l2_off", "l2_motor_visible")
        scheme_function.add_lidar_add("l2_wallet", "l2_ip", "l2_params_visible")
        scheme_function.add_port_lidar("l2_port", "l2_port_visible")
        scheme_function.add_l2_speed("l2_speed", "l2_speed_visible")
        scheme_function.add_lidar_stat("l2_packet", "l2_tgp_val", "l2_tgp_range", "l2_perf_visible")

def node_edge():
    with dpg.node(label="Edge", tag="node_ed"):
        scheme_function.add_status("ed_status_but", "ed_status")
        scheme_function.add_ip_wallet("ed_wallet", "ed_ip", param_co.state_hu["edge"]["add"], "ed_ip_visible")
        #scheme_function.add_edge_id("ed_edge_id")
        #scheme_function.add_country("ed_country")

        scheme_connection.add_sock_client_i("ed_sock_client")

        scheme_connection.add_sock_server_i("ed_sock_server")
        scheme_function.add_port_fixe("ed_sock_server_port", "ed_sock_port_visible")

        scheme_connection.add_http_client_i("ed_http_client")
        scheme_connection.add_http_server_i("ed_http_server")
        scheme_function.add_port_fixe("ed_http_server_port", "ed_http_port_visible")

def node_ve():
    with dpg.node(label="Data processing", tag="node_ve"):
        scheme_function.add_status("ve_status_but", "ve_status")
        scheme_function.add_ip_wallet("ve_wallet", "ve_ip", "localhost", "ve_ip_visible")
        scheme_function.add_velo_option("ve_opt_slam", "ve_opt_view", "ve_opt_reset")
        scheme_connection.add_sock_server_o("ve_sock_server")
        scheme_function.add_port_fixe("ve_sock_server_port", "ve_sock_port_visible")
        scheme_connection.add_http_server_o("ve_http_server")
        scheme_function.add_port_fixe("ve_http_server_port", "ve_http_port_visible")

def node_ai():
    with dpg.node(label="AI", tag="node_ai"):
        scheme_function.add_status("ai_status_but", "ai_status")
        scheme_function.add_ip_wallet("ai_wallet", "ai_ip", "localhost", "ai_ip_visible")
        scheme_function.add_ai_param_height("ai_lidar_height")
        scheme_function.add_ai_param_thres("ai_threshold")
        scheme_connection.add_http_server_o("ai_http_server")
        scheme_function.add_port_fixe("ai_http_server_port", "ai_http_port_visible")

def node_sncf():
    with dpg.node(label="SNCF", tag="node_sncf"):
        scheme_function.add_status("sncf_status_but", "sncf_status")
        scheme_function.add_ip_wallet("sncf_wallet", "sncf_ip", param_co.state_hu["sncf"]["add"], "sncf_ip_visible")
        scheme_function.add_input("MQTT", "sncf_mqtt_broker")
        scheme_function.add_port_sncf("sncf_broker_port", "ai_sncf_port_visible")
        scheme_function.add_mqtt_topic("sncf_mqtt_topic", "sncf_mqtt_topic_visible")

def node_valeo():
    with dpg.node(label="Valeo", tag="node_valeo"):
        scheme_function.add_ip("va_ip")
        scheme_connection.add_http_client_i("va_http_client")

def node_ssd():
    with dpg.node(label="SSD", tag="node_ssd"):
        scheme_function.add_status_i("ssd_input", "ssd_status_but", "ssd_status")
        scheme_function.add_ssd_active("ssd_active")
        scheme_function.add_ssd_param("ssd_path", "file_name", "ssd_path_add", "ssd_used", "ssd_total", "ssd_param_visible")
        scheme_function.add_file_info("Lidar 1", "l1_file_path", "l1_file_size", "ssd_l1_visible")
        scheme_function.add_file_info("Lidar 2", "l2_file_path", "l2_file_size", "ssd_l2_visible")

def node_data():
    with dpg.node(label="Data", tag="node_data"):
        scheme_function.add_image_sized("image_in", 300, 150)

        scheme_function.add_plot("lidar 1", "l1_yaxis", "l1_plot", "l1_plot_visible")
        scheme_function.add_plot("lidar 2", "l2_yaxis", "l2_plot", "l2_plot_visible")
        scheme_function.add_variable_simple("Frame:", "nb_frame")
        scheme_function.add_variable_simple("Prediction:", "nb_prediction")

def node_legend():
    with dpg.node(label="Legend", tag="node_legend"):
        scheme_function.add_legend_line("legend_train", "Train level components")
        scheme_function.add_legend_line("legend_edge", "Edge level components")
        scheme_function.add_legend_line("legend_cloud", "Cloud level components")
        scheme_function.add_legend_line("legend_control", "Control level components")

def node_block_train():
    with dpg.node(label="Train", tag="node_block_train"):
        scheme_function.add_image("icon_train", "icon_train_visible")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.drawlist(tag="block_train", width=450, height=200):
                pass

def node_block_edge():
    with dpg.node(label="Edge", tag="node_block_edge"):
        scheme_function.add_image("icon_server", "icon_server_visible")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.drawlist(tag="block_edge", width=350, height=550):
                pass

def node_block_cloud():
    with dpg.node(label="Cloud", tag="node_block_cloud"):
        scheme_function.add_image("icon_cloud", "icon_cloud_visible")
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.drawlist(tag="block_cloud", width=225, height=275):
                pass

def node_network():
    with dpg.node(label="KPI", tag="node_network"):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):

            with dpg.table(header_row=False, borders_innerH=False, width=350):
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()

                with dpg.table_row():
                    dpg.add_image("icon_wifi")
                    dpg.add_text("Train <-> Edge");
                    dpg.add_button(tag="train_edge_but", width=15)

            with dpg.table(header_row=True, borders_innerH=True, width=350):
                dpg.add_table_column()
                dpg.add_table_column(label="Upload")
                dpg.add_table_column(label="Download")
                dpg.add_table_column(label="Required")

                scheme_function.add_perf_throughput("perf_throughput_up_val")
                scheme_function.add_perf_latency("perf_latency_up_val", "perf_latency_do_val")
                scheme_function.add_perf_reliability("perf_reliability_up_val")
                scheme_function.add_perf_interruption("perf_interruption_val")

            with dpg.table(header_row=True, borders_innerH=True, width=350):
                dpg.add_table_column()
                dpg.add_table_column(label="Time")
                dpg.add_table_column(label="Required")
                scheme_function.add_perf_time_total("End-to-end", "perf_time_total")

        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_text("")

            with dpg.table(header_row=False, borders_innerH=False, width=350):
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()

                with dpg.table_row():
                    dpg.add_image("icon_database")
                    dpg.add_text("MongoDB");
                    dpg.add_button(tag="mongo_server_but", width=15)

            with dpg.table(header_row=False, borders_innerH=True, width=350):
                dpg.add_table_column()
                dpg.add_table_column()

                with dpg.table_row():
                    dpg.add_text("IP:");
                    dpg.add_input_text(tag="mongo_ip", label="", default_value="", width=150, on_enter=True, callback=scheme_com_mongo.callback_mongo_ip);
                with dpg.table_row():
                    dpg.add_text("Port:");
                    dpg.add_input_int(tag="mongo_port", default_value=1, width=100, callback=scheme_com_mongo.callback_mongo_port);
                with dpg.table_row():
                    dpg.add_text("Database:");
                    dpg.add_input_text(tag="mongo_db", label="", default_value="", width=150, on_enter=True, callback=scheme_com_mongo.callback_mongo_db);
                with dpg.table_row():
                    dpg.add_text("Collection:");
                    dpg.add_input_text(tag="mongo_collection", label="", default_value="", width=150, on_enter=True, callback=scheme_com_mongo.callback_mongo_collection);
                with dpg.table_row():
                    dpg.add_text("Username:");
                    dpg.add_input_text(tag="mongo_username", label="", default_value="", width=150, on_enter=True, callback=scheme_com_mongo.callback_mongo_username);

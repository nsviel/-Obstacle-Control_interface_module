#---------------------------------------------
from src.param import param_interface
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

    node_module_interface()
    node_module_capture()
    node_module_edge()
    node_train()
    node_edge_next()
    node_ve()
    node_ai()
    node_operator()
    node_cloud_car()
    node_ssd()
    node_data()
    node_network()

def node_module_interface():
    with dpg.node(label="System control interface", tag="node_co"):
        scheme_function.add_status_o("interface_input", "interface_status_but", "interface_status")
        scheme_function.add_ip("interface_ip")
        scheme_function.add_nb_thread("interface_thread", "interface_thread_visible")
        scheme_function.add_temperature("interface_temp", "interface_temp_visibile")

        scheme_function.add_choice_edge("combo_edge")

        scheme_connection.add_http_client_i("interface_http_client")

        scheme_connection.add_sock_server_i("interface_sock_server_l1")
        scheme_function.add_port_co("interface_sock_server_l1_port", "interface_port_l1_visible")

        scheme_connection.add_sock_server_i("interface_sock_server_l2")
        scheme_function.add_port_co("interface_sock_server_l2_port", "interface_port_l2_visible")

def node_module_capture():
    with dpg.node(label="Data acquisition", tag="node_py"):
        scheme_function.add_image("icon_computer", "icon_computer_visible")

        scheme_function.add_status_i("capture_input", "capture_status_but", "capture_status")
        scheme_function.add_ip_wallet("capture_wallet", "capture_ip", "-", "capture_ip_visible")
        scheme_function.add_nb_thread("capture_thread", "capture_thread_visible")

        #scheme_function.add_iperf_py()

        scheme_function.add_port_fixe_i("capture_l1_in", "capture_l1_port", "capture_l1_port_visible")
        scheme_connection.add_sock_client_o_("capture_l1_out")
        scheme_function.add_port_fixe_i("capture_l2_in", "capture_l2_port", "capture_l2_port_visible")
        scheme_connection.add_sock_client_o_("capture_l2_out")

        scheme_function.add_lidar_device("capture_l1_device", "capture_l2_device", "capture_lidar_dev_visible")

        scheme_connection.add_http_server_o("capture_http_server")
        scheme_function.add_port_fixe("capture_http_server_port", "capture_http_port_visible")

def node_module_edge():
    with dpg.node(label="Edge orchestrator", tag="node_hu"):
        scheme_function.add_status("edge_status_but", "edge_status")
        scheme_function.add_ip_wallet("edge_wallet", "edge_ip", param_interface.state_interface["edge"]["add"], "edge_ip_visible")
        scheme_function.add_nb_thread("edge_thread", "edge_thread_visible")

        scheme_function.add_edge_id("edge_edge_id", "edge_edge_id_visible")
        scheme_function.add_country("edge_country")
        scheme_function.add_mqtt("edge_mqtt_client", "edge_mqtt_client_name", "edge_mqtt_visible")
        scheme_function.add_false_alarm()

        scheme_connection.add_sock_server_io("edge_sock_server_l1_i", "edge_sock_server_l1_o")
        scheme_function.add_port_hu("edge_sock_server_l1_port", "edge_port_l1_visible")
        scheme_connection.add_sock_server_i("edge_sock_server_l2_i")
        scheme_function.add_port_hu("edge_sock_server_l2_port", "edge_port_l2_visible")

        scheme_connection.add_sock_client_source_io("edge_sock_client_l1_i", "edge_sock_client_l1_o", "edge_sock_client_l1_combo_lidar_main", "edge_src_1", "edge_src_2")
        scheme_connection.add_sock_client_source_o("edge_sock_client_l2_o", "edge_sock_client_l2_source")

        scheme_connection.add_http_client_io("edge_http_client_i", "edge_http_client_o")
        scheme_connection.add_http_server_o("edge_http_server_o")
        scheme_function.add_port_fixe("edge_http_server_port", "edge_http_port_visible")

def node_train():
    with dpg.node(label="LiDAR", tag="node_train"):
        scheme_function.add_image("icon_lidar", "icon_lidar_visible")
        scheme_function.add_geolocalization("geo_status", "geo_country")

        scheme_function.line_tagged("l1_line_visible")
        scheme_function.add_lidar_status("Lidar 1", "l1_status", "l1_activated", "l1_status_but")
        scheme_function.add_l1_motor("l1_on", "l1_off", "l1_motor_visible")
        scheme_function.add_lidar_add("l1_wallet", "l1_ip", "l1_params_visible")
        scheme_function.add_port_lidar("l1_port", "l1_port_visible")
        scheme_function.add_l1_speed("l1_speed", "l1_speedgenext_visible")
        scheme_function.add_lidar_stat("l1_packet", "l1_tgp_val", "l1_tgp_range", "l1_perf_visible")

        scheme_function.line_tagged("l2_line_visible")
        scheme_function.add_lidar_status("Lidar 2", "l2_status", "l2_activated", "l2_status_but")
        scheme_function.add_l2_motor("l2_on", "l2_off", "l2_motor_visible")
        scheme_function.add_lidar_add("l2_wallet", "l2_ip", "l2_params_visible")
        scheme_function.add_port_lidar("l2_port", "l2_port_visible")
        scheme_function.add_l2_speed("l2_speed", "l2_speedgenext_visible")
        scheme_function.add_lidar_stat("l2_packet", "l2_tgp_val", "l2_tgp_range", "l2_perf_visible")

def node_edge_next():
    with dpg.node(label="Edge", tag="node_ed"):
        scheme_function.add_status("edgenext_status_but", "edgenext_status")
        scheme_function.add_ip_wallet("edgenext_wallet", "edgenext_ip", param_interface.state_edge["edge_next"]["add"], "edgenext_ip_visible")
        #scheme_function.add_edge_id("edgenext_edge_id")
        #scheme_function.add_country("edgenext_country")

        scheme_connection.add_sock_client_i("edgenext_sock_client")

        scheme_connection.add_sock_server_i("edgenext_sock_server")
        scheme_function.add_port_fixe("edgenext_sock_server_port", "edgenext_sock_port_visible")

        scheme_connection.add_http_client_i("edgenext_http_client")
        scheme_connection.add_http_server_i("edgenext_http_server")
        scheme_function.add_port_fixe("edgenext_http_server_port", "edgenext_http_port_visible")

def node_ve():
    with dpg.node(label="Data processing", tag="node_ve"):
        scheme_function.add_status("processing_status_but", "processing_status")
        scheme_function.add_ip_wallet("processing_wallet", "processing_ip", "localhost", "processing_ip_visible")
        scheme_function.add_velo_option("processing_opt_slam", "processing_opt_view", "processing_opt_reset")
        scheme_connection.add_sock_server_o("processing_sock_server")
        scheme_function.add_port_fixe("processing_sock_server_port", "processing_sock_port_visible")
        scheme_connection.add_http_server_o("processing_http_server")
        scheme_function.add_port_fixe("processing_http_server_port", "processing_http_port_visible")

def node_ai():
    with dpg.node(label="AI", tag="node_ai"):
        scheme_function.add_status("ai_status_but", "ai_status")
        scheme_function.add_ip_wallet("ai_wallet", "ai_ip", "localhost", "ai_ip_visible")
        scheme_function.add_ai_param_height("ai_lidar_height")
        scheme_function.add_ai_param_thres("ai_threshold")
        scheme_connection.add_http_server_o("ai_http_server")
        scheme_function.add_port_fixe("ai_http_server_port", "ai_http_port_visible")

def node_operator():
    with dpg.node(label="Train operator", tag="node_operator"):
        scheme_function.add_status("trainope_status_but", "trainope_status")
        scheme_function.add_ip_wallet("trainope_wallet", "ip_operator", param_interface.state_edge["train_operator"]["add"], "ip_operator_visible")
        scheme_function.add_input("MQTT", "trainope_mqtt_broker")
        scheme_function.add_port_trainope("trainope_broker_port", "ai_trainope_port_visible")
        scheme_function.add_mqtt_topic("trainope_mqtt_topic", "trainope_mqtt_topic_visible")

def node_cloud_car():
    with dpg.node(label="cloud_car", tag="node_cloud_car"):
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
    with dpg.node(label="Processed data", tag="node_data"):
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
    with dpg.node(label="Network performance", tag="node_network"):
        # KPIs
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
                scheme_function.add_perf_reliability("perf_reliability_up_val", "perf_reliability_do_val")

            with dpg.table(header_row=True, borders_innerH=True, width=350):
                dpg.add_table_column()
                dpg.add_table_column(label="Time")
                dpg.add_table_column(label="Required")
                scheme_function.add_perf_interruption("perf_interruption_val")
                scheme_function.add_perf_time_total("End-to-end", "perf_time_total")

        # Mongo
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_text("")

            # State
            with dpg.table(header_row=False, borders_innerH=False, width=350):
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()

                with dpg.table_row():
                    dpg.add_image("icon_database")
                    dpg.add_text("MongoDB");
                    dpg.add_button(tag="mongo_server_but", width=15)

            # Parameters
            with dpg.table(tag="table_mongo", header_row=False, borders_innerH=True, width=350):
                dpg.add_table_column()
                dpg.add_table_column()

                with dpg.table_row():
                    dpg.add_text("IP");
                    dpg.add_input_text(tag="mongo_ip", label="", default_value="", width=150, on_enter=True, callback=scheme_com_mongo.callback_mongo_ip);
                with dpg.table_row():
                    dpg.add_text("Port");
                    dpg.add_input_int(tag="mongo_port", default_value=1, width=100, callback=scheme_com_mongo.callback_mongo_port);
                with dpg.table_row():
                    dpg.add_text("Database");
                    dpg.add_input_text(tag="mongo_db", label="", default_value="", width=150, on_enter=True, callback=scheme_com_mongo.callback_mongo_db);
                with dpg.table_row():
                    dpg.add_text("Collection");
                    dpg.add_input_text(tag="mongo_collection", label="", default_value="", width=150, on_enter=True, callback=scheme_com_mongo.callback_mongo_collection);
                with dpg.table_row():
                    dpg.add_text("number of data");
                    dpg.add_input_int(tag="mongo_nbdata", default_value=1, width=100, callback=scheme_com_mongo.callback_mongo_nbdata);
                with dpg.table_row():
                    dpg.add_text("Username");
                    dpg.add_input_text(tag="mongo_username", label="", default_value="", width=150, on_enter=True, callback=scheme_com_mongo.callback_mongo_username);
                with dpg.table_row():
                    dpg.add_text("Password");
                    dpg.add_input_text(tag="mongo_password", label="", default_value="", width=150, on_enter=True, callback=scheme_com_mongo.callback_mongo_password);

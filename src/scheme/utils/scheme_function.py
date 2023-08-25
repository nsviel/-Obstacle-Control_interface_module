#---------------------------------------------
from src.param import param_interface
from src.scheme.command import scheme_callback
from src.scheme.command import scheme_com
from src.scheme.command import scheme_com_lidar

import dearpygui.dearpygui as dpg

color_line = (255, 255, 255, 50)
color_info = (0, 200, 200)
color_status = (0, 200, 50)
color_title = (200, 200, 200)
color_grey = (150, 150, 150)


# Line
def line():
    with dpg.drawlist(width=125, height=1):
        dpg.draw_line([0, 0], [125, 0], color=color_line)
def line_tagged(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Static):
        with dpg.drawlist(width=125, height=1):
            dpg.draw_line([0, 0], [125, 0], color=color_line)
def line_double():
    with dpg.drawlist(width=125, height=1):
        dpg.draw_line([0, 0], [250, 0], color=color_line)

# Generic stuff
def add_text_grey(text):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_text(text, color=color_grey);
def add_attribute(text):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_text(text);
def add_temperature(tag_temp, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Temp:");
            dpg.add_text(0, tag=tag_temp, color=color_info);
            dpg.add_text("°", color=color_info);
def add_variable(text, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        line()
        with dpg.group(horizontal=True):
            dpg.add_text(text);
            dpg.add_text(0, tag=tag_, color=color_info);
def add_variable_simple(text, tag_text, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text(text);
            dpg.add_text(0, tag=tag_text, color=color_info);
def add_input(text, tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text(text, color=color_title);
def add_output(text, tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text(text);
def add_legend_line(tag_button, text):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_button(tag=tag_button, width=15)
            dpg.add_text(": " + text);
def add_status(tag_button, tag_state):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Status:");
            dpg.add_text("-", tag=tag_state, color=color_info);
            dpg.add_button(tag=tag_button, width=15)
def add_status_i(tag_input, tag_button, tag_state):
    with dpg.node_attribute(tag=tag_input, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("Status:");
            dpg.add_text("-", tag=tag_state, color=color_info);
            dpg.add_button(tag=tag_button, width=15)
def add_status_o(tag_output, tag_button, tag_state):
    with dpg.node_attribute(tag=tag_output, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("Status:");
            dpg.add_text("-", tag=tag_state, color=color_info);
            dpg.add_button(tag=tag_button, width=15)

def add_ip(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_text("127.0.0.1", tag=tag_, color=color_info);
def add_ip_wallet(tag_wallet, tag_ip, default, visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Add:");
            dpg.add_combo(param_interface.wallet_add, tag=tag_wallet, label="", default_value=default, width=120, callback=scheme_com.command_comboip)
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_text("127.0.0.1", tag=tag_ip, color=color_info);
def add_plot(label, tag_y, tag_plot, tag_visible):
    x = []
    y = []
    for i in range(0, param_interface.nb_tic):
        x.append(i)
        y.append(0)
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static, tag=tag_visible):
        with dpg.plot(no_menus=True, no_box_select=True, no_mouse_pos=True, height=50, width=300):
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, no_gridlines=True, no_tick_marks=True, no_tick_labels=True)
            dpg.add_plot_axis(dpg.mvYAxis, no_tick_labels=True, no_gridlines=True, no_tick_marks=True, tag=tag_y)
            dpg.add_plot_axis(dpg.mvYAxis, no_tick_labels=True, no_gridlines=True, no_tick_marks=True, tag=tag_y+"_0")
            dpg.set_axis_limits(tag_y, -50, 1500)
            dpg.set_axis_limits(tag_y+"_0", -50, 1500)
            dpg.add_line_series(x, y, parent=tag_y+"_0", tag=tag_y+"_line")
            dpg.add_line_series(x, y, label=label, parent=tag_y, tag=tag_plot)
def add_edge_id(tag_id, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Edge ID: [")
            dpg.add_text("", tag=tag_id, color=color_info)
            dpg.add_text("]")
def add_country(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Country: [")
            dpg.add_text("", tag=tag_, color=color_info)
            dpg.add_text("]")
def add_nb_thread(tag_thread, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Nb thread:");
            dpg.add_text(1, tag=tag_thread, color=color_info);
def add_option(label, tag_option):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text(label);
            dpg.add_checkbox(tag=tag_option, label="", default_value=True, callback=scheme_callback.callback_component_process);

# Specific stuff
def add_false_alarm():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_button(label="False alarm", callback=scheme_com.command_false_alarm)
def add_choice_edge(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        edges = ("France_1", "France_2", "Spain_1")
        dpg.add_combo(edges, tag=tag_, label="Edge", default_value="France_1", width=125, callback=scheme_com.command_false_alarm)
def add_stockage(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text("Stockage")
def add_geolocalization(tag_status, tag_geo):
    with dpg.node_attribute(tag=tag_status, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("Geo: [")
            dpg.add_text("", tag=tag_geo, color=color_info)
            dpg.add_text("]")
def add_empty_space():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            dpg.add_text("")
def add_image(tag, visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(tag=visible):
            dpg.add_image(tag)
            dpg.add_text("")
def add_image_sized(tag, width_, height_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_image(tag, width=width_, height=height_)
def add_text(text):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_text(text);
def add_velo_option(tag_slam, tag_view, tag_reset):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("SLAM:");
            dpg.add_checkbox(tag=tag_slam, label="", default_value=True, callback=scheme_callback.callback_component_process);
        with dpg.group(horizontal=True):
            dpg.add_text("View:");
            dpg.add_radio_button(("Top", "Oblique"), tag=tag_view, callback=scheme_callback.callback_component_process, horizontal=True)
        with dpg.group(horizontal=True):
            dpg.add_button(label="Reset", tag=tag_reset, width=50, callback=scheme_callback.callback_component_process_reset)
def add_iperf_train():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        with dpg.group(horizontal=True):
            dpg.add_text("Iperf");
            dpg.add_text("client", color=color_info);
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("Iperf");
            dpg.add_text("server", color=color_info);
def add_iperf_py():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        with dpg.group(horizontal=True):
            dpg.add_text("Iperf");
            dpg.add_text("server", color=color_info);
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("Iperf");
            dpg.add_text("client", color=color_info);

# Ports
def add_port_co(tag_port, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Port:");
            dpg.add_input_int(tag=tag_port, default_value=1, width=100, callback=scheme_callback.callback_module_interface);
def add_port_hu(tag_port, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Port:");
            dpg.add_input_int(tag=tag_port, default_value=1, width=100, callback=scheme_callback.callback_module_edge);
def add_port_trainope(tag_port, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Port:");
            dpg.add_input_int(tag=tag_port, default_value=1, width=100, callback=scheme_callback.callback_trainope);
def add_port_py(tag_port, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Port:");
            dpg.add_input_int(tag=tag_port, default_value=1, width=100, callback=scheme_callback.callback_module_capture);
def add_port_fixe(tag_port, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Port:");
            dpg.add_text(1, tag=tag_port, color=color_info);
def add_port_fixe_i(tag_input, tag_port, tag_visible):
    with dpg.node_attribute(tag=tag_input, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Port:");
            dpg.add_text(1, tag=tag_port, color=color_info);
def add_port_lidar(tag_port, tag_visibility):
    with dpg.node_attribute(tag=tag_visibility, attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            dpg.add_text(1, tag=tag_port, color=color_info);
            #dpg.add_input_int(tag=tag_port, default_value=1, width=100, callback=scheme_callback.callback_lidar);

# Lidar stuff
def add_lidar_device(tag_l1_dev, tag_l2_dev, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(tag=tag_visible):
            line()
            with dpg.group(horizontal=True):
                with dpg.group():
                    dpg.add_text("Lidar 1", color=color_title)
                    dpg.add_listbox(tag=tag_l1_dev, callback=scheme_com_lidar.command_l1_dev, width=125)
                with dpg.group():
                    dpg.add_text("Lidar 2", color=color_title)
                    dpg.add_listbox(tag=tag_l2_dev, callback=scheme_com_lidar.command_l2_dev, width=125)
def add_lidar_status(label, tag_con, tag_active, tag_status):
    with dpg.node_attribute(tag=tag_con, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text(label, color=color_title);
            dpg.add_button(tag=tag_status, width=15)
            dpg.add_checkbox(tag=tag_active, label="", default_value=True, indent=75, callback=scheme_callback.callback_module_capture);
def add_lidar_add(tag_wallet, tag_ip, tag_visibility):
    with dpg.node_attribute(tag=tag_visibility, attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Add:");
            dpg.add_combo(param_interface.wallet_add, tag=tag_wallet, label="", default_value="-", width=120, callback=scheme_com.command_comboip)
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_input_text(tag=tag_ip, label="", default_value="", width=150, callback=scheme_callback.callback_module_capture);
def add_l1_speed(tag_speed, tag_visibility):
    with dpg.node_attribute(tag=tag_visibility, attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Speed:");
            dpg.add_input_int(tag=tag_speed, default_value=600, step=60, min_value=0, max_value=1200, width=75, min_clamped=True, max_clamped=True, callback=scheme_com_lidar.command_l1_speed);
            dpg.add_text("rpm");
def add_l2_speed(tag_speed, tag_visibility):
    with dpg.node_attribute(tag=tag_visibility, attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Speed:");
            dpg.add_input_int(tag=tag_speed, default_value=600, step=60, min_value=0, max_value=1200, width=75, min_clamped=True, max_clamped=True, callback=scheme_com_lidar.command_l2_speed);
            dpg.add_text("rpm");
def add_l1_motor(tag_on, tag_off, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_button(label="ON ", tag=tag_on, width=50, callback=scheme_com_lidar.command_l1_start)
            dpg.add_button(label="OFF", tag=tag_off, width=50, callback=scheme_com_lidar.command_l1_stop)
def add_l2_motor(tag_on, tag_off, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_button(label="ON ", tag=tag_on, width=50, callback=scheme_com_lidar.command_l2_start)
            dpg.add_button(label="OFF", tag=tag_off, width=50, callback=scheme_com_lidar.command_l2_stop)
def add_lidar_stat(tag_packet, tag_bdw_val, tag_bdw_range, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(tag=tag_visible):
            with dpg.group(horizontal=True):
                dpg.add_text("Packet:");
                dpg.add_text(0, tag=tag_packet, color=color_info);
            with dpg.group(horizontal=True):
                dpg.add_text("Throughput:");
                dpg.add_text(0, tag=tag_bdw_val, color=color_info);
                dpg.add_text("MB/s");
            with dpg.group(horizontal=True):
                dpg.add_text("[");
                dpg.add_text(0, tag=tag_bdw_range, color=color_info);
                dpg.add_text("]");
                dpg.add_text("MB/s");

# Perf stuff
def add_perf_bandwidth(tag_val, tag_range):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Bandwidth:");
            dpg.add_text(0, tag=tag_val, color=color_info);
            dpg.add_text("[");
            dpg.add_text(0, tag=tag_range, color=color_info);
            dpg.add_text("]");
            dpg.add_text("MB/s");
def add_perf_latency(tag_val, tag_range):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Latency:");
            dpg.add_text(0, tag=tag_val, color=color_info);
            dpg.add_text("[");
            dpg.add_text(0, tag=tag_range, color=color_info);
            dpg.add_text("]");
            dpg.add_text("ms");
def add_perf_jitter(tag_val, tag_range):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Jitter:");
            dpg.add_text(0, tag=tag_val, color=color_info);
            dpg.add_text("[");
            dpg.add_text(0, tag=tag_range, color=color_info);
            dpg.add_text("]");
            dpg.add_text("ms");
def add_perf_reliability(tag_val, tag_range):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Reliability:");
            dpg.add_text(0, tag=tag_val, color=color_info);
            dpg.add_text("[");
            dpg.add_text(0, tag=tag_range, color=color_info);
            dpg.add_text("]");
            dpg.add_text("%");
def add_perf_interruption(tag_val, tag_range):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Interruption:");
            dpg.add_text(0, tag=tag_val, color=color_info);
            dpg.add_text("[");
            dpg.add_text(0, tag=tag_range, color=color_info);
            dpg.add_text("]");
            dpg.add_text("s");
def add_perf_time(text, tag):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text(text);
            dpg.add_text(0, tag=tag, color=color_info);
            dpg.add_text("ms");

# MQTT stuff
def add_mqtt(tag_client, tag_name, tag_visible):
    with dpg.node_attribute(tag=tag_client, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text("MQTT client");
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Name");
            dpg.add_input_text(tag=tag_name, default_value="ai_module", width=100, on_enter=True, callback=scheme_callback.callback_trainope)
def add_mqtt_topic(tag_topic, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True, tag=tag_visible):
            dpg.add_text("Topic");
            dpg.add_input_text(tag=tag_topic, default_value="-", width=100, on_enter=True, callback=scheme_callback.callback_trainope)

# SSD stuff
def add_ssd_active(tag_active):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("SSD saving");
            dpg.add_checkbox(tag=tag_active, label="", default_value=False, callback=scheme_callback.callback_ssd)
def add_ssd_param(tag_path, tag_name, tag_path_add, tag_used, tag_tot, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(tag=tag_visible):
            with dpg.group(horizontal=True):
                dpg.add_text("Path:")
                dpg.add_input_text(tag=tag_path, label="", default_value="", width=200, on_enter=True, callback=scheme_com.command_ssd_editing)
            with dpg.group(horizontal=True):
                dpg.add_text("Used:");
                dpg.add_text(0, tag=tag_used, color=color_info);
                dpg.add_text("/");
                dpg.add_text(0, tag=tag_tot, color=color_info);
                dpg.add_text("Gb");
            line()
            dpg.add_text("File", color=color_title)
            dpg.add_button(label="New save", width=100, callback=scheme_com.command_new_save)
            with dpg.group(horizontal=True):
                dpg.add_text("Name:");
                dpg.add_input_text(tag=tag_path_add, label="", default_value="", width=200, on_enter=True, callback=scheme_com.command_ssd_editing)
            with dpg.group(horizontal=True):
                dpg.add_text("Fullname:")
                dpg.add_text("-", tag=tag_name, color=color_info)
def add_file_info(label, tag_path, tag_size, tag_visible):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(tag=tag_visible):
            line()
            dpg.add_text(label, color=color_title)
            with dpg.group(horizontal=True):
                dpg.add_text("-", tag=tag_path, color=color_info)
            with dpg.group(horizontal=True):
                dpg.add_text("Size:")
                dpg.add_text(0, tag=tag_size, color=color_info)
                dpg.add_text("Gb");

# AI stuff
def add_ai_param_height(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Height");
            dpg.add_input_float(tag=tag_, default_value=2, width=100, step=0.1, min_value=0, callback=scheme_callback.callback_ai);
def add_ai_param_thres(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Thres");
            dpg.add_input_float(tag=tag_, default_value=0.2, width=100, step=0.01, min_value=0, max_value=1, callback=scheme_callback.callback_ai);

# Network KPIs
def add_perf_time_total(text, tag):
    with dpg.table_row():
        dpg.add_text(text)
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag, color=color_info);
            dpg.add_text("ms")
        dpg.add_text("[1.6, 2] s");
def add_perf_throughput(tag_val_up):
    with dpg.table_row():
        dpg.add_text("Throughput")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("Mb/s");
def add_perf_latency(tag_val_up, tag_val_do):
    with dpg.table_row():
        dpg.add_text("Latency")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("ms");
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_do, color=color_info);
            dpg.add_text("ms");
        dpg.add_text("< 200 ms");
def add_perf_reliability(tag_val_up, tag_val_do):
    with dpg.table_row():
        dpg.add_text("Reliability")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_up, color=color_info);
            dpg.add_text("%");
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val_do, color=color_info);
            dpg.add_text("%");
        dpg.add_text(">= 99 %");
def add_perf_interruption(tag_val):
    with dpg.table_row():
        dpg.add_text("Interruption")
        with dpg.group(horizontal=True):
            dpg.add_text(0, tag=tag_val, color=color_info);
            dpg.add_text("s");
        dpg.add_text("< 1 s");

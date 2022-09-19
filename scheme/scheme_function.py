#---------------------------------------------
from param import param_co
from scheme import scheme_callback
from scheme import scheme_command

import dearpygui.dearpygui as dpg

color_line = (255, 255, 255, 50)
color_info = (0, 200, 200)
color_status = (0, 200, 50)
color_title = (200, 200, 200)


# Generic stuff
def line():
    with dpg.drawlist(width=125, height=1):
        dpg.draw_line([0, 0], [125, 0], color=color_line)
def add_attribute(text):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_text(text);
def add_temperature(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Temp:");
            dpg.add_text(0, tag=tag_, color=color_info);
            dpg.add_text("°", color=color_info);
def add_variable(text, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        line()
        with dpg.group(horizontal=True):
            dpg.add_text(text);
            dpg.add_text(0, tag=tag_, color=color_info);
def add_variable_simple(text, tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text(text);
            dpg.add_text(0, tag=tag_, color=color_info);
def add_input(text, tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text(text, color=color_title);
def add_output(text, tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text(text);
def add_status(tag_button, tag_state):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Status:");
            dpg.add_text("-", tag=tag_state, color=color_info);
            dpg.add_button(tag=tag_button, width=15)

def add_ip(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_text("127.0.0.1", tag=tag_, color=color_info);
def add_ip_wallet(tag_wallet, tag_ip, default):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Add:");
            dpg.add_combo(param_co.wallet_add, tag=tag_wallet, label="", default_value=default, width=120, callback=scheme_command.command_comboip)
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_text("127.0.0.1", tag=tag_ip, color=color_info);
def add_port_fixe(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            dpg.add_text(1, tag=tag_, color=color_info);
def add_port_fixe_i(tag_input, tag_port):
    with dpg.node_attribute(tag=tag_input, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            dpg.add_text(1, tag=tag_port, color=color_info);
def add_plot(label, tag_y, tag_plot):
    x = []
    y = []
    for i in range(0, param_co.nb_tic):
        x.append(i)
        y.append(0)
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.plot(no_menus=True, no_box_select=True, no_mouse_pos=True, height=50, width=300):
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, no_gridlines=True, no_tick_marks=True, no_tick_labels=True)
            dpg.add_plot_axis(dpg.mvYAxis, no_tick_labels=True, no_gridlines=True, no_tick_marks=True, tag=tag_y)
            dpg.add_plot_axis(dpg.mvYAxis, no_tick_labels=True, no_gridlines=True, no_tick_marks=True, tag=tag_y+"_0")
            dpg.set_axis_limits(tag_y, -50, 1500)
            dpg.set_axis_limits(tag_y+"_0", -50, 1500)
            dpg.add_line_series(x, y, parent=tag_y+"_0", tag=tag_y+"_line")
            dpg.add_line_series(x, y, label=label, parent=tag_y, tag=tag_plot)
def add_edge_id(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Edge ID: [")
            dpg.add_text("", tag=tag_, color=color_info)
            dpg.add_text("]")
def add_country(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Country: [")
            dpg.add_text("", tag=tag_, color=color_info)
            dpg.add_text("]")
def add_nb_thread(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Nb thread:");
            dpg.add_text(1, tag=tag_, color=color_info);
def add_option(label, tag_option):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text(label);
            dpg.add_checkbox(tag=tag_option, label="", default_value=True, callback=scheme_callback.callback_velodium);

# Specific stuff
def add_false_alarm():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_button(label="False alarm", width=100, callback=scheme_command.command_false_alarm)
def add_new_save():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_button(label="New save", width=100, callback=scheme_command.command_new_save)
def add_choice_edge(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        edges = ("France_1", "France_2", "Spain_1")
        dpg.add_combo(edges, tag=tag_, label="Edge", default_value="France_1", width=125, callback=scheme_command.command_false_alarm)
def add_stockage(tag_):
    with dpg.node_attribute(tag=tag_, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text("Stockage")
def add_geolocalization(tag_):
    with dpg.node_attribute(tag="geo_input", attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("Geo: [")
            dpg.add_text("", tag=tag_, color=color_info)
            dpg.add_text("]")
def add_image(tag):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_image(tag, width=300, height=175)
def add_port_co(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            dpg.add_input_int(tag=tag_, default_value=1, width=100, callback=scheme_callback.callback_controlium);
def add_port_hu(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            dpg.add_input_int(tag=tag_, default_value=1, width=100, callback=scheme_callback.callback_hubium);
def add_port_sncf(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            dpg.add_input_int(tag=tag_, default_value=1, width=100, callback=scheme_callback.callback_sncf);
def add_port_py(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            dpg.add_input_int(tag=tag_, default_value=1, width=100, callback=scheme_callback.callback_pywardium);
def add_text(text):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_text(text);
def add_velo_option(tag_slam, tag_view):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("SLAM:");
            dpg.add_checkbox(tag=tag_slam, label="", default_value=True, callback=scheme_callback.callback_velodium);
        with dpg.group(horizontal=True):
            dpg.add_text("View:");
            dpg.add_radio_button(("Top", "Oblique"), tag=tag_view, callback=scheme_callback.callback_velodium, horizontal=True)

# Lidar stuff
def add_lidar_device(tag_l1_dev, tag_l2_dev):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        line()
        with dpg.group(horizontal=True):
            with dpg.group():
                dpg.add_text("Lidar 1", color=color_title)
                dpg.add_listbox(tag=tag_l1_dev, callback=scheme_callback.callback_pywardium, width=125)
            with dpg.group():
                dpg.add_text("Lidar 2", color=color_title)
                dpg.add_listbox(tag=tag_l2_dev, callback=scheme_callback.callback_pywardium, width=125)
def add_lidar_status(label, tag_con, tag_active, tag_status):
    with dpg.node_attribute(tag=tag_con, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        with dpg.group(horizontal=True):
            dpg.add_text(label, color=color_title);
            dpg.add_button(tag=tag_status, width=15)
            dpg.add_checkbox(tag=tag_active, label="", default_value=True, indent=75, callback=scheme_callback.callback_pywardium);
def add_lidar_info(tag_speed, tag_ip, tag_port):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        #Speed
        with dpg.group(horizontal=True):
            dpg.add_text("Speed:");
            dpg.add_input_int(tag=tag_speed, default_value=600, step=60, min_value=0, max_value=1200, width=100, min_clamped=True, max_clamped=True, callback=scheme_callback.callback_pywardium);
        #IP
        with dpg.group(horizontal=True):
            dpg.add_text("IP:");
            dpg.add_input_text(tag=tag_ip, label="", default_value="", width=200, callback=scheme_callback.callback_pywardium);
        #Port
        with dpg.group(horizontal=True):
            dpg.add_text("Port:");
            dpg.add_text(1, tag=tag_port, color=color_info);
def add_l1_motor():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_button(label="Start", width=75, callback=scheme_command.command_l1_start)
            dpg.add_button(label="Stop", width=75, callback=scheme_command.command_l1_stop)
def add_l2_motor():
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_button(label="Start", width=75, callback=scheme_command.command_l2_start)
            dpg.add_button(label="Stop", width=75, callback=scheme_command.command_l2_stop)
def add_perf(tag_packet, tag_bdw_val, tag_bdw_range):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Packet:");
            dpg.add_text(0, tag=tag_packet, color=color_info);
        with dpg.group(horizontal=True):
            dpg.add_text("Bandwidth:");
            dpg.add_text(0, tag=tag_bdw_val, color=color_info);
            dpg.add_text("MB/s");
        with dpg.group(horizontal=True):
            dpg.add_text("[");
            dpg.add_text(0, tag=tag_bdw_range, color=color_info);
            dpg.add_text("]");
            dpg.add_text("MB/s");

# MQTT stuff
def add_mqtt(tag_client, tag_name):
    with dpg.node_attribute(tag=tag_client, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        line()
        dpg.add_text("MQTT client");
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Name");
            dpg.add_input_text(tag=tag_name, default_value="ai_module", width=100, on_enter=True, callback=scheme_callback.callback_sncf)
def add_topic(tag_):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        with dpg.group(horizontal=True):
            dpg.add_text("Topic");
            dpg.add_input_text(tag=tag_, default_value="-", width=100, on_enter=True, callback=scheme_callback.callback_sncf)

# SSD stuff
def add_ssd(tag_con, tag_active, tag_path, tag_name, tag_path_add, tag_used, tag_tot):
    with dpg.node_attribute(tag=tag_con, attribute_type=dpg.mvNode_Attr_Output, shape=dpg.mvNode_PinShape_QuadFilled):
        with dpg.group(horizontal=True):
            dpg.add_text("SSD saving");
            dpg.add_checkbox(tag=tag_active, label="", default_value=True, indent=75, callback=scheme_callback.callback_ssd)
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
        dpg.add_input_text(tag=tag_path, label="", default_value="", width=200, callback=scheme_command.command_ssd_editing)
        dpg.add_input_text(tag=tag_path_add, label="", default_value="", width=200, callback=scheme_command.command_ssd_editing)
        with dpg.group(horizontal=True):
            dpg.add_text("File:")
            dpg.add_text("-", tag=tag_name, color=color_info)
        with dpg.group(horizontal=True):
            dpg.add_text("Used:");
            dpg.add_text(0, tag=tag_used, color=color_info);
            dpg.add_text("/");
            dpg.add_text(0, tag=tag_tot, color=color_info);
            dpg.add_text("Gb");
def add_file_info(label, tag_path, tag_size):
    with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
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

#---------------------------------------------
from src.scheme.utils import scheme_function
from src.scheme.utils import scheme_connection
from src.scheme.command import scheme_com_mongo

import dearpygui.dearpygui as dpg


def design_node():
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

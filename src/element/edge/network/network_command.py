#---------------------------------------------
from src.param import param_control
from src.connection.HTTPS import https_client_get
from src.connection.HTTPS import https_client_post
from src.connection.HTTPS import https_client_con
from src.utils import saving
from src.element.misc.wallet import wallet_logic

import dearpygui.dearpygui as dpg


def callback_mongodb_state():
    param_control.state_network["mongodb"]["ip"] = dpg.get_value("mongo_ip")
    param_control.state_network["mongodb"]["port"] = dpg.get_value("mongo_port")
    param_control.state_network["mongodb"]["database"] = dpg.get_value("mongo_db")
    param_control.state_network["mongodb"]["collection"] = dpg.get_value("mongo_collection")
    param_control.state_network["mongodb"]["username"] = dpg.get_value("mongo_username")
    param_control.state_network["mongodb"]["password"] = dpg.get_value("mongo_password")
    param_control.state_network["mongodb"]["nb_data"] = dpg.get_value("mongo_nbdata")

    https_client_post.post_state("network", param_control.state_network)

def update_database():
    dpg.set_value("mongo_ip", param_control.state_network["mongodb"]["ip"])
    dpg.set_value("mongo_port", param_control.state_network["mongodb"]["port"])
    dpg.set_value("mongo_db", param_control.state_network["mongodb"]["database"])
    dpg.set_value("mongo_collection", param_control.state_network["mongodb"]["collection"])
    dpg.set_value("mongo_username", param_control.state_network["mongodb"]["username"])
    dpg.set_value("mongo_password", param_control.state_network["mongodb"]["password"])
    dpg.set_value("mongo_nbdata", param_control.state_network["mongodb"]["nb_data"])

#---------------------------------------------
from src.param import param_control
from src.connection.HTTPS import https_client_get
from src.connection.HTTPS import https_client_post
from src.connection.HTTPS import https_client_con
from src.utils import saving
from src.element.misc.wallet import wallet_logic

import dearpygui.dearpygui as dpg


def callback_mongo_ip():
    https_client_post.post_param_value("edge", "mongo", "ip", dpg.get_value("mongo_ip"))

def callback_mongo_port():
    https_client_post.post_param_value("edge", "mongo", "port", dpg.get_value("mongo_port"))

def callback_mongo_db():
    https_client_post.post_param_value("edge", "mongo", "database", dpg.get_value("mongo_db"))

def callback_mongo_collection():
    https_client_post.post_param_value("edge", "mongo", "collection", dpg.get_value("mongo_collection"))

def callback_mongo_username():
    https_client_post.post_param_value("edge", "mongo", "username", dpg.get_value("mongo_username"))

def callback_mongo_password():
    https_client_post.post_param_value("edge", "mongo", "password", dpg.get_value("mongo_password"))

def callback_mongo_nbdata():
    https_client_post.post_param_value("edge", "mongo", "nb_data", dpg.get_value("mongo_nbdata"))

def update_database():
    dpg.set_value("mongo_ip", param_control.state_network["mongo"]["ip"])
    dpg.set_value("mongo_port", param_control.state_network["mongo"]["port"])
    dpg.set_value("mongo_db", param_control.state_network["mongo"]["database"])
    dpg.set_value("mongo_collection", param_control.state_network["mongo"]["collection"])
    dpg.set_value("mongo_username", param_control.state_network["mongo"]["username"])
    dpg.set_value("mongo_password", param_control.state_network["mongo"]["password"])
    dpg.set_value("mongo_nbdata", param_control.state_network["mongo"]["nb_data"])

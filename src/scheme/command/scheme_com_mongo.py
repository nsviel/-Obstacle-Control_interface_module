#---------------------------------------------
from src.param import param_interface
from src.HTTPS import https_client_get
from src.HTTPS import https_client_post
from src.HTTPS import https_client_con
from src.SOCK import sock_server
from src.misc import saving
from src.misc import wallet

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

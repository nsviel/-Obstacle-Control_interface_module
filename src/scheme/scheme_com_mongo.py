#---------------------------------------------
from src.param import param_co
from src.HTTPS import https_client_get
from src.HTTPS import https_client_post
from src.HTTPS import https_client_con
from src.SOCK import sock_server
from src.misc import saving
from src.misc import wallet

import dearpygui.dearpygui as dpg


def callback_mongo_ip():
    https_client_post.post_param_value("hu", "mongo", "ip", dpg.get_value("mongo_ip"))

def callback_mongo_port():
    https_client_post.post_param_value("hu", "mongo", "port", dpg.get_value("mongo_port"))

def callback_mongo_db():
    https_client_post.post_param_value("hu", "mongo", "database", dpg.get_value("mongo_db"))

def callback_mongo_collection():
    https_client_post.post_param_value("hu", "mongo", "collection", dpg.get_value("mongo_collection"))

def callback_mongo_username():
    https_client_post.post_param_value("hu", "mongo", "username", dpg.get_value("mongo_username"))

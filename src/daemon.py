#---------------------------------------------
from src.connection import connection
from src.element.edge.data import data_image
from src.gui.scheme import scheme_update
from src.connection.SOCK import sock_server_l1
from src.connection.SOCK import sock_server_l2


daemon_connection = connection.Connection()
daemon_image = data_image.Data_image()
daemon_scheme = scheme_update.Scheme_update()
daemon_socket_l1 = sock_server_l1.Socket_l1()
daemon_socket_l2 = sock_server_l2.Socket_l2()

def start_daemons():
    daemon_connection.start_daemon()
    daemon_socket_l1.start_daemon()
    daemon_socket_l2.start_daemon()
    daemon_image.start_daemon()
    daemon_scheme.start_daemon()

def stop_daemons():
    daemon_connection.stop_daemon()
    daemon_socket_l1.stop_daemon()
    daemon_socket_l2.stop_daemon()
    daemon_image.stop_daemon()
    daemon_scheme.stop_daemon()

#! /usr/bin/python
#---------------------------------------------


class Hubium:
    # State
    status = "Offline"
    ip = "127.0.0.1"
    jstat = {}

    # Hubium
    sock_server_port = 1
    sock_client_port = 1
    http_server_port = 1
    nb_frame = 0
    nb_prediction = 0

    # SNCF
    sncf_broker_connected = False
    sncf_broker_ip = "127.0.0.1"
    sncf_broker_port = 1
    sncf_mqtt_topic = "ai_obstacle"

    # Edge
    edge_connected = False
    edge_ip = "127.0.0.1"
    edge_port = 1

    # Valeo
    valeo_connected = False
    valeo_ip = "127.0.0.1"
    valeo_port = 1

    # Velodium
    velo_connected = False
    velo_sock_server_port = 1

    # AI
    ai_connected = False

    def reset(self):
            self.status = "Offline"
            self.sncf_broker_connected = False
            self.edge_connected = False
            self.vale_connected = False
            self.velo_connected = False
            self.ai_connected = False

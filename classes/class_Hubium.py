#! /usr/bin/python
#---------------------------------------------


class Hubium:
    # State
    #--------------------
    status = "Offline"
    ip = "127.0.0.1"
    #--------------------

    # Hubium
    sock_server_port = 1
    sock_client_port = 1
    http_server_port = 1

    # MQTT
    mqtt_connected = False
    mqtt_topic = "ai_obstacle"
    mqtt_ip = "127.0.0.1"
    mqtt_port = 1

    # Edge
    edge_connected = False
    edge_ip = "127.0.0.1"
    edge_port = 1

    # Valeo
    vale_connected = False
    valeo_ip = "127.0.0.1"
    valeo_port = 1

    # Velodium
    velo_connected = False
    velo_port = 1

    # AI
    ai_connected = False

    def reset(self):
            self.status = "Offline"
            self.ip = "127.0.0.1"
            self.sock_server_port = 1
            self.sock_client_port = 1
            self.http_server_port = 1
            self.mqtt_connected = False
            self.mqtt_topic = "ai_obstacle"
            self.mqtt_ip = "127.0.0.1"
            self.mqtt_port = 1
            self.edge_connected = False
            self.edge_ip = "127.0.0.1"
            self.edge_port = 1
            self.vale_connected = False
            self.valeo_ip = "127.0.0.1"
            self.valeo_port = 1
            self.velo_connected = False
            self.velo_port = 1
            self.ai_connected = False

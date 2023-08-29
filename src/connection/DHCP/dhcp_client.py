#---------------------------------------------
import dhcppython


def ask_for_ip():
    client = dhcppython.client.DHCPClient(interface="enp0s8")
    lease = client.get_lease(mac_addr="de:ad:be:ef:c0:de", broadcast=True, relay=None, server="255.255.255.255", options_list=None)
    print(lease)

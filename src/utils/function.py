#---------------------------------------------
import string
import random


def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def check_port_compatibility(port_1, port_2):
    ok_1 = check_port_goodness(port_1)
    ok_2 = check_port_goodness(port_2)
    ok_3 = True
    if(port_1 == port_2):
        print("[error] Ports must not be the same")
        ok_3 = False
    if(ok_1 and ok_2 and ok_3):
        return True
    else:
        return False

def check_port_goodness(port):
    if(port > 0):
        return True
    else:
        print("[error] Port must be under 0")
        return False

#---------------------------------------------
import string
import random


def id_generator(size=15, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def check_port_compatibility(port_1, port_2):
    ok_1 = check_port_goodness(port_1)
    ok_2 = check_port_goodness(port_2)
    if(ok_1 and ok_2 and port_1 != port_2):
        return True
    else:
        return False

def check_port_goodness(port):
    if(port > 0):
        return True
    else:
        return False

#---------------------------------------------
from src.element.misc.wallet import wallet_ID
from src.element.misc.wallet import wallet_window


# Generic LiDAR class
class Wallet:
    def __init__(self):
        self.ID = wallet_ID.Wallet_ID()
        self.window = wallet_window.Wallet_window(self.ID)

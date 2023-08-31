#---------------------------------------------
from src.element.misc.wallet import wallet_ID
from src.element.misc.wallet import wallet_window
from src.element.misc.wallet import wallet_logic


# Generic LiDAR class
class Wallet:
    def __init__(self):
        self.ID = wallet_ID.Wallet_ID()
        wallet_logic.read_wallet_file()
        self.window = wallet_window.Wallet_window(self.ID)

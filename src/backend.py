from src.band import Band
from src.membro import Membro
from src.custom_exceptions import UtenteNonRegistrato
from src.custom_exceptions import BandNonRegistrata



class Backend:
    def __init__(self) -> None:
        self.band: dict[str, Band] = {}
        self.users: dict[str, Membro] = {}

    # --------------------------------------------------------------
    # MODULI PER IL DI ESISTENZA
    # -------------------------------------------------------------- 
    
    def is_user_registered(self, username: str) -> bool:
            if username not in self.users.keys():
                return False
            else:
                return True 


    def is_band_registered(self, band_id: str) -> bool:
        if band_id not in self.users.keys():
            return False
        else:
            return True 







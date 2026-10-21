from .canzone import Canzone
from .enums import Key, Stato
from .custom_exceptions import CanzoneGiaPresenteException, CanzoneNonTrovataException



class Repertorio:

    def __init__(self):
        self.brani: dict[str, Canzone] = {}

    def aggiungi(self, nuova_canzone: Canzone) -> None:
        if nuova_canzone.id_canzone in self.brani:
            raise CanzoneGiaPresenteException(f"La canzone {nuova_canzone.titolo} risulta già presente al repertorio")
        self.brani[nuova_canzone.id_canzone] = nuova_canzone

    def rimuovi(self, da_rimuovere: Canzone) -> Canzone:
        if da_rimuovere.id_canzone not in self.brani:
            raise CanzoneNonTrovataException("La canzone specificata non è presente nel repertorio")
        return self.brani.pop(da_rimuovere.id_canzone)

    def getCanzone(self,id_canzone : str):
        return self.brani[id_canzone]
    


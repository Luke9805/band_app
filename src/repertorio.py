from .elemento_repertorio import ElementoRepertorio
from .canzone import Canzone
from .enums import Key, Stato




class Repertorio:
    def __init__(self):
        self.elementi: dict[str, ElementoRepertorio] = {}

    def aggiungi_brano(
        self, 
        nome: str,
        autore: str,
        bpm: float,
        key: Key, 
        tonalita: Key, 
        stato: Stato = Stato.NEW,
        ) -> ElementoRepertorio:
        
        nuova_canzone = Canzone(nome, autore, bpm, key)
        item = ElementoRepertorio(nuova_canzone, stato)
            
        self.elementi[nuova_canzone.id_canzone] = item
        return item
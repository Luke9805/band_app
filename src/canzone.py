from typing import override
import uuid
from .enums import Key  # O Tonalita, a seconda di come hai chiamato l'Enum
from .custom_exceptions import ValidazioneCampoError


class Canzone:
    def __init__(self, titolo: str, autore: str, bpm: float, key: Key, note=None):
        
        # Check di sicurezza
        if titolo == "" or not str(titolo).strip():
            raise ValidazioneCampoError("Il titolo è obbligatorio!")

        if autore == "" or not str(autore).strip():
            raise ValidazioneCampoError("L'autore è obbligatorio!")

        if bpm <= 0:
            raise ValidazioneCampoError("Il BPM deve essere un numero maggiore di 0!")
        
        if not isinstance(key, Key):
            raise ValidazioneCampoError("La chiave/tonalità deve essere un valore valido dell'Enum Key!")

        # Assegnazione attributi
        self.id_canzone: str = str(uuid.uuid4())
        self.titolo = titolo.strip()
        self.autore = autore.strip()
        self.bpm = bpm
        self.key = key
        self.note = note.strip() if note else ""

    def cambia_key(self, nuova_key: Key):
        if not isinstance(nuova_key, Key):
            raise ValidazioneCampoError("La nuova tonalità deve essere un valore valido dell'Enum Key!")
        self.key = nuova_key
    
    def cambia_bpm(self, nuovo_bpm: float):
        if nuovo_bpm is None or nuovo_bpm <= 0:
            raise ValidazioneCampoError("Il nuovo BPM deve essere un numero maggiore di 0!")
        self.bpm = nuovo_bpm



    @override
    def __str__(self):
        return f"{self.titolo} {self.autore} {self.bpm} {self.key}"
    
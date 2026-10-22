from typing import override

from src.canzone import Canzone

from .custom_exceptions import ValidazioneCampoError
from .repertorio import Repertorio
from .enums import Strumento
from src import repertorio

class Membro:

    def __init__(self,
     username: str,
     nome: str,
     cognome: str,
     #mail: str, # da aggiungere
     #password: str, #da aggiungere
     strumenti: list[Strumento] | None = None
     ):
        

        if username == "" or not str(username).strip():
            raise ValidazioneCampoError("L'username è obbligatorio e non può contenere solo spazi!")

        if nome == "" or not str(nome).strip():
            raise ValidazioneCampoError("Il nome è obbligatorio e non può contenere solo spazi!")

        if cognome == "" or not str(cognome).strip():
            raise ValidazioneCampoError("Il cognome è obbligatorio e non può contenere solo spazi!")

        self.nome: str = nome
        self.cognome: str = cognome
        self.username: str = username
        self.strumenti: list[Strumento] = strumenti if strumenti is not None else []
        self.repertorio_personale: Repertorio = Repertorio()


    def aggiungi_a_repertorio_personale(self, nuova_canzone: Canzone):
        self.repertorio_personale.aggiungi(nuova_canzone)

    def rimuovi_da_repertorio_personale(self, nuova_canzone: Canzone) -> Canzone:
        return self.repertorio_personale.rimuovi(nuova_canzone)

    def aggiungi_strumento(self, strumento: Strumento):
        if strumento not in self.strumenti:
            self.strumenti.append(strumento)
        

    @override
    def __str__(self):
        strumento = ", ".join(str(strumento) for strumento in self.strumenti)
        return f"{self.nome} {self.cognome} (@{self.username}) {strumento}"

    def cambia_nome(self, nuovo_nome: str):
        self.nome = nuovo_nome

    def cambia_cognome(self, nuovo_cognome: str):
        self.nome = nuovo_cognome



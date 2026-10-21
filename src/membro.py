from typing import override

from .custom_exceptions import ValidazioneCampoError
from .repertorio import Repertorio
from .enums import Strumento

class Membro:

    def __init__(self,
     username: str,
     nome: str,
     cognome: str,
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
        self.repertorio: Repertorio = Repertorio()




    def aggiungi_strumento(self, strumento: Strumento):
        if strumento not in self.strumenti:
            self.strumenti.append(strumento)
        

    @override
    def __str__(self):
        return f"{self.nome} {self.cognome} (@{self.username}) {self.strumenti}"

from .custom_exceptions import ValidazioneCampoError

class Membro:
    def __init__(self, username: str, nome: str, cognome: str, strumenti=None):
        
        if username is None or not str(username).strip():
            raise ValidazioneCampoError("L'username è obbligatorio e non può contenere solo spazi!")

        if nome is None or not str(nome).strip():
            raise ValidazioneCampoError("Il nome è obbligatorio e non può contenere solo spazi!")

        if cognome is None or not str(cognome).strip():
            raise ValidazioneCampoError("Il cognome è obbligatorio e non può contenere solo spazi!")

        self.nome = nome
        self.cognome = cognome
        self.username = username
        self.strumenti = strumenti if strumenti is not None else []


    def aggiungi_strumento(self, strumento):
        self.strumenti.append(strumento)

    def __str__(self):
        return f"{self.nome} {self.cognome} (@{self.username})"
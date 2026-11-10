import uuid
from src.custom_exceptions import ValidazioneCampoError, MessaggioNonPresente

class Chat:

    def __init__(self,
    id_band: str,
    ) -> None:
        self.id_band = id_band
        self.messaggi: dict[str, Messaggio] = {} 



    def scrivi_messaggio(self, mittente: str, contenuto: str)->None:
        if contenuto == "" or not str(contenuto).strip():
            raise ValidazioneCampoError("Non è possibile mandare un messaggio vuoto")
            
            # aggiungere il controllo sul membro presente nella band. 

        nuovo_messaggio = Messaggio(mittente, contenuto, False)
        self.messaggi[nuovo_messaggio.id_messaggio] = nuovo_messaggio



    def elimina_messaggio(self, id_messaggio: str) -> Messaggio:
        if id_messaggio not in self.messaggi:
            raise MessaggioNonPresente("Il seguente messaggio non è presente nella chat")
        
        return self.messaggi.pop(id_messaggio)


    def modifica_messaggio(self, id_messaggio: str, contenuto_modificato: str) -> None:
        if contenuto_modificato == "" or not str(contenuto_modificato).strip():
            raise ValidazioneCampoError("Non è possibile modificare con un messaggio vuoto")

        if id_messaggio not in self.messaggi:
            raise MessaggioNonPresente("Il seguente messaggio non è presente nella chat")


        self.messaggi[id_messaggio].contenuto = contenuto_modificato



class Messaggio:

    def __init__(self,
    mittente: str,
    contenuto: str,
    is_important: bool
    ) -> None:

        self.id_messaggio: str = str(uuid.uuid4()) 
        self.contenuto: str = contenuto
        self.mittente: str = mittente
        
    





        
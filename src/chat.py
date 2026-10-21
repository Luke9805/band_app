import uuid

class Chat:

    def __init__(self,
    id_band: str,
    ) -> None:
        self.id_band = id_band



class Messaggio:

    def __init__(self,
    mittente: str,
    contenuto: str,
    is_important: bool
    ) -> None:

        self.id_messaggio: str = str(uuid.uuid4()) 
        self.contenuto = contenuto
        self.mittente = mittente





        
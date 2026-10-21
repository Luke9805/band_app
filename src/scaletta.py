from .canzone import Canzone
from .elemento_repertorio import ElementoRepertorio
from .enums import Stato

class Scaletta:

    def __init__(self, 
    elementi: list[Canzone] | None = None
    ) -> None:
        
        self.elementi: list[Canzone] = [] if elementi is None else list(elementi)


    def aggiungi_da_repertorio(self, 
        id_repertorio: str,
        id_canzone:str
        ) -> None:
        pass

        



    def aggiungi_alla_scaletta(self, canzone: Canzone):
        Stato.NEW

        self.elementi.append(canzone)


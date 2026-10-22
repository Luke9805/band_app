from .canzone import Canzone
from .enums import Stato

class Scaletta:

    def __init__(self, 
    elementi: list[Canzone] | None = None
    ) -> None:
        
        self.elementi: list[Canzone] = [] if elementi is None else list(elementi)



    def aggiungi_alla_scaletta(self, canzone: Canzone):
        Stato.NEW
        self.elementi.append(canzone)


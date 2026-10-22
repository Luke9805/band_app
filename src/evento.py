from .scaletta import Scaletta
from .canzone import Canzone
from datetime import datetime
import zoneinfo


class Evento:

    def __init__(self, quando: datetime, luogo: str) -> None:
        self.quando = quando
        self.luogo = luogo
        self.scaletta = Scaletta()


    def aggiungi_a_scaletta(self, nuova_canzone: Canzone):
        self.scaletta.aggiungi_alla_scaletta

    


        
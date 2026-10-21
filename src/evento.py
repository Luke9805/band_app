from datetime import datetime
import zoneinfo


class Evento:

    def __init__(self, quando: datetime, luogo: str) -> None:
        self.quando = quando
        self.luogo = luogo
        self.scaletta = Scaletta()

    


        
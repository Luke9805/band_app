from .enums import Stato
from .custom_exceptions import ValidazioneCampoError
from .canzone import Canzone

class ElementoRepertorio:
    def __init__(
        self,
        canzone: Canzone,
        stato: Stato,
        ):
        # security check
        if not isinstance(canzone, Canzone):
            raise ValidazioneCampoError("Canzone non valida!")
        if not isinstance(stato, Stato):
            raise ValidazioneCampoError("Stato brano non valido!")
        
        self.stato = stato
        self.canzone = canzone




    def cambia_stato(self, nuovo_stato: Stato):
        if not isinstance(nuovo_stato, Stato):
            raise ValidazioneCampoError("Stato non valido!")
        self.stato = nuovo_stato
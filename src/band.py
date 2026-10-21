from typing import override
from .canzone import Canzone
from .membro import Membro
from .repertorio import Repertorio
from .evento import Evento

class Band:

    def __init__(self, 
    nome_band: str,
    primo_membro: Membro | None = None
    ) -> None:

        self.nome_band: str = nome_band
        self.membri_band: list[Membro] = [primo_membro] if primo_membro is not None else []
        self.repertorio_band: Repertorio = Repertorio()
        self.eventi: list[Evento]


    def aggiungi_membro(self, nuovo_membro: Membro) -> None:
        if nuovo_membro not in self.membri_band:
            self.membri_band.append(nuovo_membro)

    def aggingi_a_repertorio_band(self, nuova_canzone: Canzone):
        self.repertorio_band.aggiungi(nuova_canzone)

    def agggingi_a_repertorio_band(self, nuova_canzone: Canzone) -> Canzone:
        return self.repertorio_band.rimuovi(nuova_canzone)

    @override
    def __str__(self) -> str:
        nomi = "\n ".join(str(membro) for membro in self.membri_band)
        return f"Band {self.nome_band},\n membri {nomi}"
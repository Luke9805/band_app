from typing import override

from .membro import Membro
from .repertorio import Repertorio

class Band:

    def __init__(self, 
    nome_band: str,
    primo_membro: Membro | None = None,
    ) -> None:

        self.nome_band: str = nome_band
        self.membri_band: list[Membro] = [primo_membro] if primo_membro is not None else []
        self.repertorio: Repertorio = Repertorio()


    def aggiungi_membro(self, nuovo_membro: Membro) -> None:
        if nuovo_membro not in self.membri_band:
            self.membri_band.append(nuovo_membro)

    @override
    def __str__(self) -> str:
        nomi = "\n ".join(str(membro) for membro in self.membri_band)
        return f"Band {self.nome_band},\n membri {nomi}"
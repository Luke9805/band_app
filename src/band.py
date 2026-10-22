from typing import override
from .canzone import Canzone
from .membro import Membro
from .repertorio import Repertorio
from .evento import Evento
from src import repertorio

class Band:

    def __init__(self, 
    nome_band: str,
    membri_iniziali: list[Membro] | None = None
    ) -> None:

        self.nome_band: str = nome_band
        self.membri_band: list[Membro] = list(membri_iniziali) if membri_iniziali is not None else []
        self.repertorio_band: Repertorio = Repertorio()
        self.eventi: list[Evento]


    def aggiungi_membro(self, nuovo_membro: Membro) -> None:
        if nuovo_membro not in self.membri_band:
            self.membri_band.append(nuovo_membro)

    def copia_su_repertorio_band(self, username:str, id_canzone: str) -> None:
        membro_trovato = None
        for m in self.membri_band:
            if m.username == username:
                try: 
                    da_repertorio = m.repertorio_personale.getCanzone(id_canzone)
                    da_aggiungere = Canzone(da_repertorio.titolo, da_repertorio.autore, da_repertorio.bpm, da_repertorio.key)
                    self.repertorio_band.aggiungi(da_aggiungere)
                except:
                    print("La canzone specificata non è stata trovata")



    def aggingi_a_repertorio_band(self, nuova_canzone: Canzone):
        self.repertorio_band.aggiungi(nuova_canzone)

    def agggingi_a_repertorio_band(self, nuova_canzone: Canzone) -> Canzone:
        return self.repertorio_band.rimuovi(nuova_canzone)

    @override
    def __str__(self) -> str:
        nomi = "\n ".join(str(membro) for membro in self.membri_band)
        return f"Band {self.nome_band},\n membri {nomi}"
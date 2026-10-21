from src.membro import Membro
from src.canzone import Canzone
from src.enums import Strumento, Key
from src.band import Band

m1 = Membro("Lukexx9805", "Luca", "Salvigni", [Strumento.BASS, Strumento.ELECTRIC_GUITAR])
m2 = Membro("Antonius544", "Antonio", "Giacomino", [Strumento.BASS, Strumento.ELECTRIC_GUITAR])
m1.aggiungi_strumento(Strumento.BATTERY)


can = Canzone("La canzone migliore del mondo", "Hammon", 120, Key.A_MAJ, "hammon ama javascript")

rags = Band("RAGS", m1)

rags.aggiungi_membro(m2)





print(m1)
print(can)
print(rags)

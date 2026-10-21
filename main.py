from src.membro import Membro
from src.canzone import Canzone
from src.enums import Strumento, Key


m1 = Membro("Lukexx9805", "Luca", "Salvigni", [Strumento.BASS, Strumento.ELECTRIC_GUITAR])

m1.aggiungi_strumento(Strumento.BATTERY)
m1.aggiungi_strumento(Strumento.BATTERY)

can = Canzone("La canzone migliore del mondo", "Hammon", 120, Key.A_MAJ, "hammon ama javascript")





print(m1)
print(can)

from datetime import datetime

from src.canzone import Canzone
from src.membro import Membro
from src.band import Band
from src.evento import Evento
from src.enums import Key, Strumento


def main():
    # 1. Creazione dei 7 Membri
    membro1 = Membro("amanialmic", "Serena", "Muscaridola", [Strumento.PIANO])
    membro2 = Membro("antonius", "Antonio", "Giacomino", [Strumento.ELECTRIC_GUITAR])
    membro3 = Membro("stefikind", "Stefano", "Gentile", [Strumento.BASS, Strumento.BATTERY])
    membro4 = Membro("mattexx", "Matteo", "Sarra", [Strumento.BATTERY])
    membro5 = Membro("lello", "Leonardo", "Ielpo", [Strumento.ELECTRIC_GUITAR])
    membro6 = Membro("lukxx9805", "Luca", "Salvigni", [Strumento.ELECTRIC_GUITAR])
    membro7 = Membro("alefont", "Alessandro", "Fontana")

    tutti_i_membri = [
        membro1, membro2, membro3, membro4, 
        membro5, membro6, membro7
    ]

    # 2. Creazione della Band passando subito la lista dei 7 membri
    mia_band = Band("RAGS", membri_iniziali=tutti_i_membri)

    # 3. Creazione delle 6 Canzoni
    canzoni = [
        Canzone("Bohemian Rhapsody", "Queen", 72, Key.B_MAJ),
        Canzone("Sultans of Swing", "Dire Straits", 148, Key.D_MIN),
        Canzone("Paranoid", "Black Sabbath", 164, Key.E_MIN),
        Canzone("Rock You Like a Hurricane", "Scorpions", 124, Key.E_MIN),
        Canzone("Symphony of Destruction", "Megadeth", 140, Key.F_SHARP_MIN),
        Canzone("Do I Wanna Know?", "Arctic Monkeys", 85, Key.G_MIN)
    ]

    canzone_personale = Canzone("American Idiot", "Green Day", 186, Key.G_SHARP_MAJ)
    membro6.aggiungi_a_repertorio_personale(canzone_personale)
    # 4. Popolamento repertorio band
    for c in canzoni:
        mia_band.aggingi_a_repertorio_band(c)


    mia_band.copia_su_repertorio_band(membro6.username, canzone_personale.id_canzone)
    

    # 5. Creazione dell'Evento
#   concerto = Evento(
#        quando=datetime(2026, 7, 15, 21, 0), 
#       luogo="Ivvillino di samuele, Matera"
#    )

    # 6. Output di verifica
    print("=== INFO BAND ===")
    print(mia_band)
    print(f"\nNumero membri totali: {len(mia_band.membri_band)}")

    print("\n=== REPERTORIO BAND ===")
    print(f"Numero canzoni: {len(mia_band.repertorio_band.brani)}")
    for canzone in mia_band.repertorio_band.brani.values():
        print(f"- {canzone}")

#    print("\n=== EVENTO ===")
#   print(f"Concerto a {concerto.luogo} il {concerto.quando.strftime('%d/%m/%Y %H:%M')}")


if __name__ == "__main__":
    main()
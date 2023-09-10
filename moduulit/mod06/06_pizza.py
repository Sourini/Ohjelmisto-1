# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math
ekapizza = False

def pizzahinta(hintaf, halkaisijaf):
    pizzakoko = ((halkaisijaf / 200) ** 2) * math.pi
    yksikkohinta = hintaf / pizzakoko
    return yksikkohinta


for i in range(2):
    hinta = int(input(f'syötä {i + 1}. pizzan hinta: '))
    halkaisija = int(input(f'syötä {i + 1}. pizzan halkaisija senttimetreinä'))
    if not ekapizza:
        pizza1 = pizzahinta(hinta, halkaisija)
        ekapizza = True
    else:
        pizza2 = pizzahinta(hinta, halkaisija)

if pizza1 < pizza2:
    print('Ensimmäinen pizza on parempi vastine rahalle.')
else:
    print('toinen pizza on  parempi vastine rahalle.')

#----------------------------------------------------------------------------------
# ILMAN FOR-LOOPPIA
#hinta = int(input('syötä ensimmäisen pizzan hinta: '))
#halkaisija = int(input('syötä ensimmäisen pizzan halkaisija senttimetreinä'))
#pizza1 = pizzahinta(hinta, halkaisija)
#hinta = int(input('syötä toisen pizzan hinta: '))
#halkaisija = int(input('syötä toisen pizzan halkaisija senttimetreinä'))
#pizza2 = pizzahinta(hinta, halkaisija)

#if pizza1 > pizza2:
#    print('toinen pizza on halvempi')
#else:
#    print('ensimmäinen pizza on halvempi')
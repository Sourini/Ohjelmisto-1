# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random

class Auto:

    nopeus = 0
    kuljettu_matka = 0
    aika = 0

    def __init__(self, rt, hn):
        self.rt = rt
        self.hn = hn

    def kiihdytä(self):
        Auto.nopeus = Auto.nopeus + random.randint(-10, 15)
        if Auto.nopeus > self.hn:
            Auto.nopeus = self.hn
        if Auto.nopeus < 0:
            Auto.nopeus = 0
        Auto.kuljettu_matka = Auto.kuljettu_matka + Auto.nopeus



lista = []


for i in range(10):
    numero = random.randint(100, 200)
    autojuttu = Auto(f'ABC-{i}', numero)
    lista.append(autojuttu.kiihdytä())



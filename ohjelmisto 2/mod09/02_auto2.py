# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h
# ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

class Auto:
    nopeus = 0
    kuljettu_matka = 0
    def __init__(self, rt, hn):
        self.rt = rt
        self.hn = hn

    def kiihdytä(self, nm):
        Auto.nopeus = Auto.nopeus + nm
        if Auto.nopeus > self.hn:
            Auto.nopesu = self.hn
        if Auto.nopeus < 0:
            Auto.nopeus = 0

auto1 = Auto("ABC-123", 142)
auto1.kiihdytä(30)
print(f'auton nopeus on {Auto.nopeus}km/h')
auto1.kiihdytä(70)
print(f'auton nopeus on {Auto.nopeus}km/h')
auto1.kiihdytä(50)
print(f'auton nopeus on {Auto.nopeus}km/h')
auto1.kiihdytä(-200)
print(f'auton nopeus on {Auto.nopeus}km/h')
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
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nm):
        self.nopeus = self.nopeus + nm
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.kuljettu_matka += aika * self.nopeus

autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

kilpailu_loppu = False
tunnit = 0

# Race loop
while not kilpailu_loppu:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_loppu = True
            break
    tunnit += 1

# Print the results
print(f"\nKilpailu loppui {tunnit} tunnin jälkeen.")
print("\n\n{:<16} {:<14} {:<20} {:<20}".format("Rekisteritunnus", "Nopeus (km/h)", "Kuljettu matka (km)", "Huippunopeus (km/h)"))
for auto in autot:
    print("{:<16} {:<14} {:<20} {:<20}".format(auto.rekisteritunnus, auto.nopeus, auto.kuljettu_matka, auto.huippunopeus))


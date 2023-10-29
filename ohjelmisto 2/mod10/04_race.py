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


autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i + 1}", random.randint(100, 200)))


class Kilpailu:
    def __init__(self, nimi, pituus, autolista):
        self.nimi = nimi
        self.pituus = pituus
        self.autolista = autolista
        self.aika = 0
        self.kilpailu_loppu = False

    def tunti_kuluu(self):
        self.aika += 1
        for auto in self.autolista:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("\n\n{:<16} {:<14} {:<20} {:<20}".format("Rekisteritunnus", "Nopeus (km/h)", "Kuljettu matka (km)",
                                                       "Huippunopeus (km/h)"))
        for auto in self.autolista:
            print("{:<16} {:<14} {:<20} {:<20}".format(auto.rekisteritunnus, auto.nopeus, auto.kuljettu_matka,
                                                       auto.huippunopeus))

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.kuljettu_matka >= self.pituus:
                self.kilpailu_loppu = True
                return self.kilpailu_loppu


romuralli = Kilpailu('Suuri Romuralli', 8000, autot)

while not romuralli.kilpailu_ohi():
    for i in range(10):
        romuralli.tunti_kuluu()
    if not romuralli.kilpailu_ohi():
        romuralli.tulosta_tilanne()

print(f"\n\n\nKilpailu loppui {romuralli.aika} tunnin jälkeen.")
romuralli.tulosta_tilanne()
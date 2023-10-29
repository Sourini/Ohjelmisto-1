# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
# pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
# kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:
#
# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
# eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
#
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
#
# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
# kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
#
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen
# sen jälkeen, kun kilpailu on päättynyt.


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
# Laajenna ohjelmaa siten, että mukana on kulje-metodi,
# joka saa parametrinaan tuntimäärän. Metodi kasvattaa kuljettua matkaa
# sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

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

    def kulje(self, aika):
        Auto.kuljettu_matka = aika * Auto.nopeus

auto1 = Auto("ABC-123", 142)
auto1.kiihdytä(30)
auto1.kulje(1)
print(f'auton nopeus on {Auto.nopeus}km/h')
print(f'auto on kulkenut {Auto.kuljettu_matka}km')
auto1.kiihdytä(70)
auto1.kulje(2)
print(f'auton nopeus on {Auto.nopeus}km/h')
print(f'auto on kulkenut {Auto.kuljettu_matka}km')
auto1.kiihdytä(50)
auto1.kulje(3)
print(f'auton nopeus on {Auto.nopeus}km/h')
print(f'auto on kulkenut {Auto.kuljettu_matka}km')
auto1.kiihdytä(-200)
auto1.kulje(0.02)
print(f'auton nopeus on {Auto.nopeus}km/h')
print(f'auto on kulkenut {Auto.kuljettu_matka}km')
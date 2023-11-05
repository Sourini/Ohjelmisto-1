# Extend the previously written Car class by adding two subclasses: ElectricCar and GasolineCar.
# Electric cars have the capacity of the battery in kilowatt-hours as their property.
# Gasoline cars have the volume of the tank in liters as their property.
# Write initializers for the subclasses. For example, the initializer of electric cars receives the registration number,
# maximum speed and battery capacity as its parameter. It calls the initializer of the base class to set the first two
# properties and then sets its capacity. Write a main program where you create one electric car
# (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars,
# make them drive for three hours and print out the values of their kilometer counters.

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

    def print_information(self):
        print(f'\n\nRegistration number: {self.rekisteritunnus}\nTop speed: {self.huippunopeus}km/h\nDistance traveled: {self.kuljettu_matka}km')

class Gas(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, volume):
        super().__init__(rekisteritunnus, huippunopeus)
        self.volume = volume

    def print_information(self):
        super().print_information()
        print(f'Tank volume: {self.volume}l')

class Electric(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, battery):
        super().__init__(rekisteritunnus, huippunopeus)
        self.battery = battery

    def print_information(self):
        super().print_information()
        print(f'Battery capacity: {self.battery}kWh')


autot = []
autot.append(Electric("ABC-15", 180, 52.5))
autot.append(Gas("ACD-123", 165, 32.3))

for i in range(3):
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

for auto in autot:
    auto.print_information()
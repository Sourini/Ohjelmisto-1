# Extend the program again by adding a method fire_alarm that does not receive any parameters and
# moves all elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.


class Elevator:
    def __init__(self, elevn, topf, botf, ):
        self.elevn = elevn
        self.topf = topf
        self.botf = botf
        self.curf = botf

    def go_to_floor(self, tarf=0):
        if self.curf == tarf:
            print(f'The elevator #{self.elevn} is already on the {self.curf} floor.')
        if self.curf < tarf:
            for i in range(tarf - self.curf):
                Elevator.floor_up(self)
                print(f'The elevator #{self.elevn} is currently on floor {self.curf}')
        if self.curf > tarf:
            for i in range(self.curf - tarf):
                Elevator.floor_down(self)
                print(f'The elevator #{self.elevn} is currently on floor {self.curf}')

    def floor_up(self):
        self.curf += 1

    def floor_down(self):
        self.curf -= 1


class Building:

    def __init__(self, topf, botf, elevs):
        self.elevators = []
        for i in range(elevs):
            self.elevators.append(Elevator(f'{i + 1}', topf, botf))

    def run_elevator(self, elevn, tarf):
        self.elevn = self.elevators[elevn - 1]
        self.elevn.go_to_floor(tarf)

    def fire_alarm(self):
        for i in range(len(self.elevators)):
            self.elevn = self.elevators[i]
            self.elevn.go_to_floor(0)
            print(f'Fire Alarm! Elevator #{i+1} moved to the bottom floor.')


building = Building(8, 0, 3)

building.run_elevator(3, 6)
building.run_elevator(2, 4)
building.run_elevator(1, 3)
building.fire_alarm()
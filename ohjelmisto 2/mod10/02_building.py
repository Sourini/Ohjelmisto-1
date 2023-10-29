# Extend the previous program by creating a Building class.
# The initializer parameters for the class are the numbers of the bottom and top floors
# and the number of elevators in the building. When a building is created,
# the building creates the required number of elevators.
# The list of elevators is stored as a property of the building.
# Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
# In the main program, write the statements for creating a new building and running the elevators of the building.

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


building = Building(8, 0, 3)

building.run_elevator(3, 6)
building.run_elevator(2, 4)
building.run_elevator(1, 3)
building.run_elevator(3, 5)
building.run_elevator(2, 1)
building.run_elevator(1, 8)

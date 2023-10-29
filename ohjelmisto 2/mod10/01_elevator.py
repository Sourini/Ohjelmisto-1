# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or
# floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or
# down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program,
# tell it to move to a floor of your choice and then back to the bottom floor.


class Elevator:
    def __init__(self, topf, botf,):
        self.topf = topf
        self.botf = botf
        self.curf = botf
    def go_to_floor(self, tarf=0):
        if self.curf < tarf:
            for i in range(tarf - self.curf):
                Elevator.floor_up(self)
        if self.curf > tarf:
            for i in range(self.curf - tarf):
                Elevator.floor_down(self)
        if self.curf == tarf:
            return
    def floor_up(self):
        self.curf += 1
        print(f'you are currently on floor {self.curf}')
    def floor_down(self):
        self.curf -= 1
        print(f'you are currently on floor {self.curf}')


elevator = Elevator(5,0)

elevator.go_to_floor(3)
elevator.go_to_floor()
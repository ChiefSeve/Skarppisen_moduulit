#  Talo
import random

#  Elevator class
class Elevator:
    def __init__(self, b_floor, t_floor, number):
        self.bottom_floor = b_floor
        self.top_floor = t_floor
        self.current_floor = b_floor
        self.number = number

    def floor_up(self, floor):
        while self.current_floor < floor:
            self.current_floor = self.current_floor + 1
            print(f'Elevator {self.number} is at floor', self.current_floor)

    def floor_down(self, floor):
        while self.current_floor > floor:
            self.current_floor = self.current_floor - 1
            print(f'Elevator {self.number} is at floor', self.current_floor)

    def change_floor(self, floor_number):
        if floor_number > self.current_floor:
            print('Going up!')
            self.floor_up(floor_number)
        elif floor_number < self.current_floor:
            print('Going down!')
            self.floor_down(floor_number)
        else:
            print('error')


#  Building class
class Building:
    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.elevators = []

    def create_elevators(self, elevators):
        new_elevators_list = []
        i = 1
        while len(new_elevators_list) < elevators:
            new_elevator = Elevator(self.bottom_floor, self.top_floor, i)
            i = i + 1
            new_elevators_list.append(new_elevator)
        self.elevators = new_elevators_list

    def move_elevator(self, floor, elevator_number):
        for elevator in self.elevators:
            if elevator.number == elevator_number:
                elevator.change_floor(floor)

    def fire_alarm(self):
        print('ALERT! ALL ELEVATORS GOING TO BOTTOM FLOOR')
        for elevator in self.elevators:
            elevator.change_floor(0)


building = Building(10, 0)
building.create_elevators(5)
j  = 1
while j <= len(building.elevators):
    building.move_elevator(random.randint(1, 10), j)
    j = j + 1
building.fire_alarm()

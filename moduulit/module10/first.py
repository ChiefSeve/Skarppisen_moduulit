#  Hissi

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self, floor):
        while self.current_floor < floor:
            print('current floor', self.current_floor)
            self.current_floor = self.current_floor + 1

    def floor_down(self, floor):
        while self.current_floor > floor:
            print('Current floor', self.current_floor)
            self.current_floor = self.current_floor - 1

    def change_floor(self, floor_number):
        if floor_number > self.current_floor:
            print('Going up!')
            self.floor_up(floor_number)
        elif floor_number < self.current_floor:
            print('Going down!')
            self.floor_down(floor_number)
        else:
            print('error')


new_elevator = Elevator(0, 10)

new_elevator.change_floor(5)
print(new_elevator.current_floor, 'CURRENT')


new_elevator.change_floor(new_elevator.bottom_floor)
print(new_elevator.current_floor, 'CURRENT')

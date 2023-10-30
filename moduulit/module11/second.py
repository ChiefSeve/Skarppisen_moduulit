# Car

class Car:
    def __init__(self, licence_plate, top_speed, current_speed=0, odo=0):
        self.licence_plate = licence_plate
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.odo = odo


class ElectricCar(Car):
    def __init__(self, kwh, licence_plate, top_speed):
        self.kwh = kwh
        self.capacity = 50
        super().__init__(licence_plate, top_speed)

    def drive_for_three_hours(self):
        self.current_speed = 90
        self.odo = self.current_speed * 3
        print(self.odo, 'ELECTRIC CAR ODO')


class PetrolCar(Car):
    def __init__(self, consumption, licence_plate, top_speed):
        self.consumption = consumption
        self.tank = 50
        super().__init__(licence_plate, top_speed)

    def drive_for_three_hours(self):
        self.current_speed = 120
        self.odo = self.current_speed * 3
        print(self.odo, 'PETROL CAR ODO')


def main_app():
    new_e_car = ElectricCar(52.5, 'ABC-15', 180)
    new_p_car = PetrolCar(32.3, 'ACD-123', 165)

    new_e_car.drive_for_three_hours()
    new_p_car.drive_for_three_hours()


main_app()
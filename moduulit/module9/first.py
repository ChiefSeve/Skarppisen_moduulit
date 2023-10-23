class Car:
    def __init__(self, licencePlate, topSpeed, currentSpeed=0, odo=0):
        self.licencePlate = licencePlate
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
        self.odo = odo


myCar = Car("ABC-123", "123Km/h")
print(myCar.licencePlate, myCar.topSpeed, myCar.currentSpeed, myCar.odo, 'DO YOU LIKE MY CAR?')

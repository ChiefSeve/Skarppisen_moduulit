class Car:

    def __init__(self, licencePlate, topSpeed, currentSpeed=0, odo=0):
        self.licencePlate = licencePlate
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
        self.odo = odo

    def travel(self, travelTime):
        newDistance = self.currentSpeed * travelTime
        self.odo = self.odo + newDistance


myCar = Car("ABC-123", 123, 60, 2000)
myCar.travel(1.5)
print(myCar.odo)

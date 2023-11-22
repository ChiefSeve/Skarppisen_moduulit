class Car:

    def __init__(self, licencePlate, topSpeed, currentSpeed=0):
        self.licencePlate = licencePlate
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed

    def accelerate(self, speedChange):
        if speedChange < 0:
            if (self.currentSpeed + speedChange) >= 0:
                self.currentSpeed = self.currentSpeed + speedChange
                return
            else:
                self.currentSpeed = 0
                return print('UNDER 0')
        elif 0 < speedChange < self.topSpeed:
            if (self.currentSpeed + speedChange) < self.topSpeed:
                self.currentSpeed = self.currentSpeed + speedChange
                return
            else:
                self.currentSpeed = self.topSpeed
                return print('Too fast man')


myCar = Car("ABC-123", 123)
myCar.accelerate(30)
print(myCar.currentSpeed)
myCar.accelerate(70)
print(myCar.currentSpeed)
myCar.accelerate(50)
print(myCar.currentSpeed)
myCar.accelerate(-200)
print(myCar.currentSpeed)

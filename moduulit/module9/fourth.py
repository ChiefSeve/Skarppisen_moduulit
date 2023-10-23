import random
import tabulate

class Car:

    def __init__(self, licencePlate, topSpeed, currentSpeed=0, odo=0):
        self.licencePlate = licencePlate
        self.topSpeed = topSpeed
        self.currentSpeed = currentSpeed
        self.odo = odo

    def accelerate(self, speedChange):
        if speedChange < 0:
            if (self.currentSpeed + speedChange) >= 0:
                self.currentSpeed = self.currentSpeed + speedChange
                return
            else:
                self.currentSpeed = 0
                return
        elif 0 < speedChange < self.topSpeed:
            if (self.currentSpeed + speedChange) < self.topSpeed:
                self.currentSpeed = self.currentSpeed + speedChange
                return
            else:
                self.currentSpeed = self.topSpeed
                return

    def travel(self, travelTime):
        newDistance = self.currentSpeed * travelTime
        self.odo = self.odo + newDistance


racers = []
i = 1
while i <= 10:
    newRacer = Car(f'ABC-{i}', random.randint(100, 200))
    racers.append(newRacer)
    i += 1


def speedster():
    while True:
        for racer in racers:
            if racer.odo <= 10000:
                racer.accelerate(random.randint(-10, 15))
                racer.travel(1)
            else:
                return racer.licencePlate


speedster()
# Somewhat nice looking leaderboard, could be better
for finalResult in racers:
    print(tabulate.tabulate([[finalResult.licencePlate, finalResult.currentSpeed, finalResult.topSpeed, finalResult.odo]], headers=['LICENCE PLATE', 'CURRENT SPEED', 'TOP SPEED', 'TOTAL DISTANCE'], tablefmt='orgtbl'),'\n\n')
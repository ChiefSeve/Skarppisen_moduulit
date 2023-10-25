#  Kilpailu
import random

import tabulate


class Racer:

    def __init__(self, licence_plate, top_speed, current_speed=0, odo=0):
        self.licence_plate = licence_plate
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.odo = odo

    def accelerate(self, speed_change):
        if speed_change < 0:
            if (self.current_speed + speed_change) >= 0:
                self.current_speed = self.current_speed + speed_change
                return
            else:
                self.current_speed = 0
                return
        elif 0 < speed_change < self.top_speed:
            if (self.current_speed + speed_change) < self.top_speed:
                self.current_speed = self.current_speed + speed_change
                return
            else:
                self.current_speed = self.top_speed
                return


class Tournament:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.participants = []
        self.time = 0

    def hour_passes(self, racer):
        new_distance = racer.current_speed * 1
        racer.odo = racer.odo + new_distance
        racer.accelerate(random.randint(-10, 15))
        self.time = self.time + 1

    def print_status(self):
        for result in self.participants:
            print(
                tabulate.tabulate(
                    [[result.licence_plate, result.current_speed, result.top_speed, result.odo]],
                    headers=['LICENCE PLATE', 'CURRENT SPEED', 'TOP SPEED', 'TOTAL DISTANCE'], tablefmt='orgtbl'),
                '\n\n')

    def tournament_over(self):
        while True:
            for racer in self.participants:
                if racer.odo <= self.length:
                    tourney.hour_passes(racer)
                    if self.time % 10 == 0:
                        tourney.print_status()
                else:
                    return False


tourney = Tournament('Suuri romuralli', 8000)


def new_participant():
    i = 1
    racers = []
    while i <= 10:
        racer = Racer(f'ABC-{i}', random.randint(100, 200))
        racers.append(racer)
        i = i + 1
    tourney.participants = racers


def speedster_v2():
    new_participant()
    tourney.tournament_over()


speedster_v2()

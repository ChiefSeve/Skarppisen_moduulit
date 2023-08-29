import random
import math


def piste():
    input_n = int(input("Anna pisteiden määrä: "))
    i = 0
    n = 0
    while i <= input_n:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if ((math.pow(x, 2)) + (math.pow(y, 2))) <= 1:
            n = n + 1
        i = i + 1
    area = 4 * n / input_n
    print("Pi:n arvo: ", area)


piste()

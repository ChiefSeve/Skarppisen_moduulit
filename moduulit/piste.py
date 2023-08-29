import random
import math
# import time
# start_time = time.time()


def piste():
    input_n = input('Anna pisteiden määrä: ')
    try:
        input_n = int(input_n)
        if input_n > 0:
            i = 0
            n = 0
            while i <= input_n:
                x = random.uniform(-1, 1)
                y = random.uniform(-1, 1)
                if ((math.pow(x, 2)) + (math.pow(y, 2))) <= 1:
                    n = n + 1
                i = i + 1
            area = 4 * n / input_n
            print(f'Pi:n arvo on {area}')
            # print('___ %s seconds ___' % (time.time() - start_time))
        else:
            print('Annoit alle tai 0 pistettä')
    except ValueError:
        print(f'Ei ollut numero')


piste()

def foo():
    input_array = []
    while True:
        if len(input_array) < 5:
            i = input(f'Insert 5 numbers ')
            try:
                i = int(i)
                if i % 2 == 1:
                    print(f'{i} uneven')
                    input_array.append(i)
                else:
                    print(f'{i} even')
                    input_array.append(i)
            except ValueError:
                print(f'{i} NaN')
                break
        else:
            print(f'array length over')
            total = 0
            for k in input_array:
                total = total + k
            average = total / len(input_array)
            print(f'total is {total}')
            print(f'Average is {average:2.1f}')
            break


# foo()

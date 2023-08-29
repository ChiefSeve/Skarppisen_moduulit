def karkausvuosi():
    year = int(input('Vuosi: '))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return print('Karkausvuosi')
            else:
                return print('Ei ole karkausvuosi')
        else:
            return print('Karkausvuosi')
    else:
        return print('Ei ole karkausvuosi')


karkausvuosi()

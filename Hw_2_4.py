def vvod(message):
    rez = -1
    while rez:
        try:
            rez = int(input(message))
        except:
            print('Не число')
            rez = -1
        finally:
            return rez


number0 = vvod('Введите первое число = ')
number1 = vvod('Введите второе число = ')
listN = vvod('Введите диапозон чисел = ')
ind = 0
proiz = 1


for i in range(-listN, listN):
    ind = ind + 1
    if ind == number0 or ind == number1:
        proiz = proiz * i

print(proiz)
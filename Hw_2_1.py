print('Введите вещественное число = ')
number = input()
sum = 0

for i in number:
    if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        sum = sum + int(i)

print(sum)

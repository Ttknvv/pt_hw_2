#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму

number = int(input('Введите число = '))
prod = 0

for i in range(1, number + 1):
    prod = prod + round((1 + 1/i)**i)

print(prod)
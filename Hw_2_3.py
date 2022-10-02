number = int(input('Введите число = '))
prod = 0

for i in range(1, number + 1):
    prod = prod + round((1 + 1/i)**i)

print(prod)
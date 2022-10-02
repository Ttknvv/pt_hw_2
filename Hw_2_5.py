#Реализуйте алгоритм перемешивания списка.

import random

def rand(first, second):
    return random.randint(first, second)

mass = []
mass0 = []
num = 10

for i in range(num):
    mass.append(i)

ind = 0
sch = 0
while sch != len(mass):
    ind = rand(0, len(mass))
    if ind not in mass0:
        mass0.append(ind)
        sch = sch + 1

for i in range(0, len(mass0)):
    print(mass0[i])
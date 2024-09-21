from random import random

mass = []
for i in range (3):
    mass.append((round(random() * 10)))
    print(mass[i])

flag = False
for i in range(len(mass)):
    if mass[i] % 2 == 1:
        flag = True
        break
if flag:
    print("В массиве есть нечетные числа")
else:
    print("В массиве нет нечетных чисел")
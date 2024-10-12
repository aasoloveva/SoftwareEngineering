#Сгенерировать массив рандомных целых чисел от 0 до 1000, удалить из него и вывести на экран три самых больших значения.
from pprint import pprint
from random import random

mass = [int(random()*1001) for x in range(10)]
pprint(mass)
for i in range(3):
    print(mass.pop(mass.index(max(mass))))
pprint(mass)
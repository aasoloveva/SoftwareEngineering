from random import random

def throwDice():
    dice = round(random() * 5 + 1)
    print("Выпало число ", dice)
    if dice == 5 or dice == 6: print("Вы победили")
    elif dice == 3 or dice == 4:
        print("Кидаем ещё раз")
        throwDice()
    elif dice == 1 or dice == 2: print("Вы проиграли")
    else: print("Ошибка")

if __name__ == '__main__':
    throwDice()
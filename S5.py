mass = []
try:
    with open("Birthdays.txt", "r") as f:
        mass += f.readlines()
except FileNotFoundError:
    with open("Birthdays.txt", "w") as f:
        pass
for i in range(len(mass)):
    #Дмитрий : 31.12
    mass[i] = mass[i].split(":")
    mass[i][1] = list(map(int, mass[i][1].split(".")))
#print(mass)

command = input("Введите \"Добавить\", чтобы добавить новый день рождения, или \"Список\", чтобы посмотреть список дней рождений. \"Готово\", чтобы завершить работу.\n")
while command != "Готово":
    if command == "Добавить":
        name = input("Введите имя: ")
        date = list(input("Введите день и месяц в формате \"31.12\": ").split("."))

        mass.append([name, date])
        mass = sorted(mass, key = lambda a: int(a[1][0])) #day
        mass = sorted(mass, key = lambda b: int(b[1][1])) #month

        with open("Birthdays.txt", "w") as f:
            for x in mass:
                f.write(f"{x[0]} : {x[1][0]}.{x[1][1]}\n")
    elif command == "Список":
        for x in mass:
            print(f"{x[0]} : {x[1][0]}.{x[1][1]}")
    elif command == "Готово":
        pass
    else:
        print("Неизвестная команда.")
    command = input()
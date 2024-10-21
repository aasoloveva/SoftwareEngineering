rashodi = []
with open("rashodi.txt", "r", encoding="Windows-1251") as f:
    rashodi += f.readlines()
with open("rashodi.txt", "a", encoding="Windows-1251") as f:
    command = ""
    print("Чтобы показать список введите \"Список\", чтобы добавить новый элемент введите \"Добавить\", чтобы закончить введите \"Готово\"")
    while command != "Готово":
        command = input()
        if command == "Список":
            if rashodi:
                print(f"Занесенные расходы:")
                for x in rashodi:
                    print(x, end="")
                print("")
            else:
                print("Список пуст.")
        elif command == "Добавить":
            newitem = input("Введите дату: ")
            newitem += " " + input("Введите название объекта: ")
            newitem += " - " + input("Введите сумму: ") + "р"
            rashodi.append("\n" + newitem)
            f.write("\n" + newitem)
        elif command == "Готово":
            pass
        else:
            print("Неизвестная команда.")
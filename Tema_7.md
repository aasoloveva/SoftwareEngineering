# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме #7 выполнил(а):
- Соловьева Анна Антоновна
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | - |
| Задание 2 | - | - |
| Задание 3 | - | - |
| Задание 4 | - | - |
| Задание 5 | - | - |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L1.png)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().
```python
with open("input.txt", "r") as f:
    print(f.readline())
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L2.png)
## Выводы
- `open()` открывает файл. Режимы: "r", "w", "a" - read, write, append.
- `open()` в режиме "r" позволяет читать содержимое файла.
- `close()` закрывает файл.
- `readline()` считывает одну строку из файла.

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().
```python
f = open("input.txt", "r")
print(f.readlines())
f.close()
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L3.png)
## Выводы
- `readlines()` считывает все строки из файла в виде массива строк.

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().
```python
with open("input.txt", "r") as f:
    print(f.readlines())
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L4.png)
## Выводы
- `with open() as f:` открывает файл, всегда закрывает файл после окончания конструкции.

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
```python
with open("input.txt", "r") as f:
    for i in f:
        print(i, end="")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L5.png)
## Выводы
`for i in f` можно перебрать строки из файла через `for`.

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.
```python
with open("input.txt", "a+") as f:
    f.write("\nLine 3")
with open ("input.txt", "r") as f:
    for l in f:
        print(l, end="")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L6_1.png)
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L6_2.png)
## Выводы
- `open()` в режиме "a" дописывает в конец файла.
- `write()` пишет в файл.

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.
```python
lines = ["one", "two", "three"]
with open ("input.txt", "w") as f:
    for l in lines:
        f.write(f"Line {l}\n")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L7_1.png)
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L7_2.png)
## Выводы
- `open()` в режиме "w" перезаписывает содержимое файла.

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print docs(directory).
```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
        print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
        print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('C:\\Users\\Lenovo\\PycharmProjects\\UNI')
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L8.png)
## Выводы
- `os.walk()` позволяет обойти директорию, включая все её поддиректории, и выполнить какое-либо действие для каждого файла.

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: <...> Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных
```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]

        if len(sought_words) == 1:
            return sought_words[0]

        return sought_words


print(longest_words('input.txt'))
print(longest_words('input2.txt'))
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L9.png)
## Выводы
Функция longest_words открывает файл с кодировкой utf-8, записывает все слова в массив words, затем записывает наибольшую длину среди слов и находит слова с этой длиной.

## Лабораторная работа №10
### Требуется создать csv-файл «rows 300.csv» со следующими столбцами:
- № - номер по порядку (от 1 до 300);
- Секунда - текущая секунда на вашем ПК:
- Микросекунда - текущая миллисекунда на часах. <br>
Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['N', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L10_1.png)
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_L10_2.png)
## Выводы
- Библиотека `csv` позволяет работать с файлами формата csv.
- Библиотеки `datetime` и `time` возволяют работать с датами и временем.

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
```python
pun = ".,?!:;\"'—()"
with open("doc.txt", "r", encoding='Windows-1251') as f:
    text = f.readlines()
for x in text:
    for y in pun:
        if y == "-" or y == "—":
            x = x.replace(y, " ")
        else:
            x = x.replace(y, "")
    #print(x)
words = []
for x in text:
    words += x.split()
maxcount = 0
maxword = ""
for x in set(words):
    if words.count(x) > maxcount:
        maxcount = words.count(x)
        maxword = x
print(f"Количество слов: {len(words)}.")
print(f"Самое частое слово: {maxword}, встречающееся {maxcount} раз.")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_S1.png)
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_S1_2png)
## Выводы
Развернутый вывод

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
```python
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
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_S2.png)
## Выводы
Развернутый вывод

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
```python
pun = ".,?!:;\"'—()"
letters = 0
words = 0
lines = 0
with open("input3.txt", "r") as f:
    text = f.readlines()
for x in text:
    for y in pun:
        x = x.replace(y, "")
    words += len(x.split())
    for y in x.split():
        letters += len(y)
lines = len(text)
print(f"{letters} letters\n{words} words\n{lines} lines")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_S3.png)
## Выводы
Развернутый вывод

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****
```python
prohibited = []
with open("input4.txt", "r") as f:
    prohibited += f.readline().split()
text = input()
textwopunct = text.lower()

for x in prohibited:
    while x in textwopunct:
        index = textwopunct.find(x)
        if index != -1:
            textwopunct = textwopunct[:index] + ("*" * len(x)) + textwopunct[index + len(x):]
            text = text[:index] + ("*" * len(x)) + text[index + len(x):]
print(text)
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/f59a4ce7305f25101009e3ae1e47045ceeddc261/img/screenshot_7_S4.png)
## Выводы
Развернутый вывод

## Самостоятельная работа №5
### У вас очень плохая память, когда дело касается дней рождений. Необходима программа, которая поможет вам создать txt-файл со списком дней рождений друзей в столбик по возрастанию дат. При последующих запусках программы и вводе новых дат, они должны вставать на свои места по возрастанию среди старых дат.
```python
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
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/7380f2c8fa781a6b2211e0891ca066697345b9b6/img/screenshot_7_S5.png)
## Выводы
Развернутый вывод

## Общие выводы по теме
Обшие выводы
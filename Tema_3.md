# Тема 3. Операторы, условия, циклы
Отчет по Теме #3 выполнил(а):
- Соловьева Анна Антоновна
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | - |
| Задание 2 | + | - |
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
### Создайте две переменные, значение которых будете вводить через консоль. Также составьте условие, в котором созданные ранее переменные будут сравниваться, если условие выполняется, то выведете в консоль «Выполняется», если нет, то «Не выполняется».
```python
a, b = int(input()), int(input())
if a >= b:
    print("Выполняется")
else:
    print("Не выполняется") 
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_1.png)
## Выводы
Для проверки выполнения какого-то условия используются операторы `if else`

## Лабораторная работа №2
### Напишите программу, которая будет определять значения переменной меньше 0, больше 0 и меньше 10 или больше 10. Это нужно реализовать при помощи одной переменной, значение которой будет вводится через консоль, а также при помощи конструкций if, elif, else.
```python
x = int(input())
if x < 0:
    print("x < 0")
elif 0 < x < 10:
    print("x > 0 and x < 10")
elif x == 10 or x == 0:
    print("x = 10 or x = 0")
else:
    print("x > 10")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_2.png)
## Выводы
Структура `if elif else` с любым количеством `elif` позволяет создать сразу несколько условий для проверки 

## Лабораторная работа №3
### 
```python
mass = [1, 3, 4, 6, 8, 9]
x = int(input())
if x in mass:
    print("Yes")
else:
    print("No")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_3_1.png)
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_3_2.png)
## Выводы
Краткие Выводы
  
## Лабораторная работа №4
### 
```python
mass = [1, 3, 4, 6, 8, 9, 15, 16, 73, 321, 322]
x = int(input())
if x in mass:
    print("Yes")
    if x % 2 == 0:
        print("Четная")
    else:
        print("Нечетная")
else:
    print("No")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_4_1.png)
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_4_2.png)
## Выводы
Краткие Выводы

## Лабораторная работа №5
### 
```python
for i in range(11):
    if i < 5:
        print(i, "< 5")
    else:
        print(i, ">= 5")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_5.png)
## Выводы
Краткие Выводы

## Лабораторная работа №6
### Напишите программу, в которой при помощи цикла for определяется есть ли переменная value в строке string и посмотрите, как работает оператор else для циклов. Самостоятельно посмотрите, что выведет программа, если значение переменной value оказалось в строке string.
```python
s = "Привет всем изучающим Python!"
sub = input()
print("Строка:", s)
for i in range(len(s)):
    if s[i] == sub:
        print("Буква есть в строке")
        break
else:
    print("Буквы в строке нету")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_6_1.png)
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_6_2.png)
## Выводы
Краткие Выводы

## Лабораторная работа №7
### Напишите программу, в которой вы наглядно посмотрите, как работает цикл for проходя в обратном порядке, то есть, к примеру не от 0 до 10, а от 10 до 0. В уже готовой программе показано вычитание из 100, а вам во время реализации программы будет необходимо придумать свой вариант применения обратного цикла.
```python
for i in range(10,-1,-1):
    print (i, end=" ")
    if i % 2 == 0:
        print("четное")
    else:
        print("нечетное")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_7.png)
## Выводы
Краткие Выводы

## Лабораторная работа №8
### Напишите программу используя цикл while, внутри которого есть какие-либо проверки, но быть осторожным, поскольку циклы while при неправильно написанных условиях могут становится бесконечными, как указано в примере далее.
```python
a = int(input())
while a >= 1:
    if a % 2 == 0:
        print("Четное")
        a //= 2
        a -= 1
    else:
        print("Нечетное")
        a -= 1
print(a)
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_8.png)
## Выводы
Краткие Выводы

## Лабораторная работа №9
### 
```python
pows = []
num = 1
power = 1
print("1    2    3    4    5")
print("---------------------")
for i in range (5):
    pows.append([])
    for j in range(5):
        pows[i].append(num ** power)
        if pows[i][j] < 10:
            print(pows[i][j], end="    ")
        elif pows[i][j] < 100:
            print(pows[i][j], end="   ")
        elif pows[i][j] < 1000:
            print(pows[i][j], end="  ")
        elif pows[i][j] < 10000:
            print(pows[i][j], end=" ")
        power += 1
    num += 1
    power = 1
    print("")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_9.png)
## Выводы
Краткие Выводы

## Лабораторная работа №10
### 
```python
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
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_10_1.png)
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/bfc5babaffc27a4d0f6b57002627334fa26e6475/img/screenshot_3_10_2.png)
## Выводы
Краткие Выводы

## Самостоятельная работа №1
### 
```python
```
### Результат.
![Меню]()
## Выводы
Краткие Выводы
- Текст задания
- Оформленный код
- Скрины консоли
- Развернутый вывод
  
## Самостоятельная работа №2
- Текст задания
- Оформленный код
- Скрины консоли
- Развернутый вывод
  
## Самостоятельная работа №3
- Текст задания
- Оформленный код
- Скрины консоли
- Развернутый вывод
  
## Самостоятельная работа №4
- Текст задания
- Оформленный код
- Скрины консоли
- Развернутый вывод
  
## Самостоятельная работа №5
- Текст задания
- Оформленный код
- Скрины консоли
- Развернутый вывод
  
## Самостоятельная работа №6
- Текст задания
- Оформленный код
- Скрины консоли
- Развернутый вывод
  
## Самостоятельная работа №7
- Текст задания
- Оформленный код
- Скрины консоли
- Развернутый вывод
  
## Самостоятельная работа №8
- Текст задания
- Оформленный код
- Скрины консоли
- Развернутый вывод
  
## Самостоятельная работа №9
- Текст задания
- Оформленный код
- Скрины консоли
- Развернутый вывод
  
## Самостоятельная работа №10
- Текст задания
- Оформленный код
- Скрины консоли
- Развернутый вывод

## Общие выводы по теме
- Развернутый вывод

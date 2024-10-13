# Тема 6. Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил(а):
- Соловьева Анна Антоновна
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | - | - |
| Задание 2 | - | - |
| Задание 3 | - | - |
| Задание 4 | - | - |
| Задание 5 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### В школе, где вы учились, узнали, что вы крутой программист и попросили написать программу для учителей, которая будет при вводе кабинета писать для него ключ доступа и статус, занят кабинет или нет. При написании программы необходимо использовать словарь (dict), который на вход получает номер кабинета, а выводит необходимую информацию. Если кабинета, который вы ввели нет в словаре, то в консоль в виде значения ключа нужно вывести "None" и виде статуса вывести "False".
```python
request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}

response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/a65b69861cf2c44217f82e419b733f09dc42b1cf/img/screenshot_6_L1.png)
## Выводы
Краткие выводы

## Лабораторная работа №2
### 
```python
from pprint import pprint

my_dict = {"First":"So easy"}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name="Михаил", age=31, weight=70,eyes_color="blue")
pprint(my_dict)
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/a65b69861cf2c44217f82e419b733f09dc42b1cf/img/screenshot_6_L2.png)
## Выводы
Краткие выводы

## Лабораторная работа №3
###
```python
input_string = "HelloWorld"
result = tuple(input_string)
print(result)
print(list(result))
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/a65b69861cf2c44217f82e419b733f09dc42b1cf/img/screenshot_6_L3.png)
## Выводы
Краткие выводы

## Лабораторная работа №4
###
```python
def personal_info(name, age, company="unnamed"):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)
bob = ("Георгий", 41, "Yandex")
personal_info(*bob)
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/a65b69861cf2c44217f82e419b733f09dc42b1cf/img/screenshot_6_L4.png)
## Выводы
Краткие выводы

## Лабораторная работа №5
###
```python
def sort_tuple(x):
    for i in x:
        if not isinstance(i, int):
            return x
    return tuple(sorted(x))


tupl1 = (5,5,3,1,9)
tupl2 = (5,5,2.1,'1',9)
print(sort_tuple(tupl1))
print(sort_tuple(tupl2))
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/a65b69861cf2c44217f82e419b733f09dc42b1cf/img/screenshot_6_L5.png)
## Выводы
Краткие выводы

## Самостоятельная работа №1
###
```python
a = input()
mass = list(map(int, a.split()))
tup = tuple(map(int, a.split()))
print(mass, tup, sep="\n")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/a65b69861cf2c44217f82e419b733f09dc42b1cf/img/screenshot_6_S1.png)
## Выводы
Развернутый вывод

## Самостоятельная работа №2
###
```python
def breaktherules(tup, x):
    mass = list(tup)
    try:
        mass.remove(x)
    except ValueError:
        return tup
    else:
        return tuple(mass)

print(breaktherules((1,2,3), 1))
print(breaktherules((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(breaktherules((2, 4, 6, 6, 4, 2), 9))
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/a65b69861cf2c44217f82e419b733f09dc42b1cf/img/screenshot_6_S2.png)
## Выводы
Развернутый вывод

## Самостоятельная работа №3
###
```python
s="111235930184619"

def create_dict(string):
    d = {x: string.count(str(x)) for x in range(10)}
    res = {}
    mass = sorted(d, key=d.get)[::-1]
    mass = mass[0:3]
    mass = sorted(mass)[::-1]
    for i in mass:
        res.update({i:string.count(str(i))})
    return res
print(create_dict(s))
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/a65b69861cf2c44217f82e419b733f09dc42b1cf/img/screenshot_6_S3.png)
## Выводы
Развернутый вывод

## Самостоятельная работа №4
###
```python
def smth(tupl, id):
    try:
        first = tupl.index(id)
        try:
            second = tupl.index(id, first + 1)
            return tupl[first:second + 1]
        except ValueError:
            second = len(tupl) - 1
            return tupl[first:second + 1]
    except ValueError:
        return tuple()
print(smth((1,2,3),8))
print(smth((1,8,3,4,8,8,9,2),8))
print(smth((1,2,8,5,1,2,9),8))
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/a65b69861cf2c44217f82e419b733f09dc42b1cf/img/screenshot_6_S4.png)
## Выводы
Развернутый вывод

## Самостоятельная работа №5
### Сгенерировать массив рандомных целых чисел от 0 до 1000, удалить из него и вывести на экран три самых больших значения.
```python
from pprint import pprint
from random import random

mass = [int(random()*1001) for x in range(10)]
pprint(mass)
for i in range(3):
    print(mass.pop(mass.index(max(mass))))
pprint(mass)
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/a65b69861cf2c44217f82e419b733f09dc42b1cf/img/screenshot_6_S5.png)
## Выводы
Развернутый вывод

## Общие выводы по теме
Обшие выводы

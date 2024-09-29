# Тема 4. Функции и модули
Отчет по Теме #4 выполнил(а):
- Соловьева Анна Антоновна
- ИВТ-22-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | - | - |
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
### 
```python
def smth():
    print(25**2)

if __name__ == "__main__":
    smth()
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/43852dd97c5b4bcc1935e9d53dab4b3f567486f0/img/screenshot_4_1.png)
## Выводы
краткие выводы

## Лабораторная работа №2
### 
```python
def smth():
    return 25**2

if __name__ == "__main__":
    print(smth())
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/43852dd97c5b4bcc1935e9d53dab4b3f567486f0/img/screenshot_4_2.png)
## Выводы
краткие выводы

## Лабораторная работа №3
### 
```python
def smth(x, y):
    return x ** y

for i in range(3):
    for j in range(2, 5):
        print(i, "^", j, "=", smth(i, j))

```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/43852dd97c5b4bcc1935e9d53dab4b3f567486f0/img/screenshot_4_3.png)
## Выводы
краткие выводы
  
## Лабораторная работа №4
### 
```python
def multiply(*args):
    res = 1;
    for i in args:
        res *= i
    return res

print(multiply(1, 2, 3, 4, 5, 6))
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/43852dd97c5b4bcc1935e9d53dab4b3f567486f0/img/screenshot_4_4.png)
## Выводы
краткие выводы

## Лабораторная работа №5
### 
```python
def fruits(**kwargs):
    for fruit, amount in kwargs.items():
        print(f"{fruit}: {amount}")

if __name__ == "__main__":
    fruits(apples = 1, oranges = 5, bananas = 2)
    fruits(**{"mandarins": 10, "pears": 2})
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/43852dd97c5b4bcc1935e9d53dab4b3f567486f0/img/screenshot_4_5.png)
## Выводы
краткие выводы

## Лабораторная работа №6
### 
```python
def mean(num):
    return sum(num) / float(len(num))

def nums(**kwargs):
    for x, y in kwargs.items():
        print(f"{x} mean: {mean(y)}")

if __name__ == "__main__":
    nums(x=[1,2,3,4,5], y=[6,7,8], z=[9,10,11,12])
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/43852dd97c5b4bcc1935e9d53dab4b3f567486f0/img/screenshot_4_6.png)
## Выводы
краткие выводы

## Лабораторная работа №7
### 
- import_7.py
```python
def hw():
    print("Hello, World!")
```
7.py
```python
from import_7 import hw

if __name__ == "__main__":
    hw()
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/43852dd97c5b4bcc1935e9d53dab4b3f567486f0/img/screenshot_4_7.png)
## Выводы
краткие выводы

## Лабораторная работа №8
### 
```python
from math import sqrt, sin, cos

def main():
    value = int(input('Введите значение: '))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == '__main__':
    main()
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/43852dd97c5b4bcc1935e9d53dab4b3f567486f0/img/screenshot_4_8.png)
## Выводы
краткие выводы

## Лабораторная работа №9
### 
```python
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}.\nДень недели - {dt.today().isoweekday()}"
    )
    n = int(input("Введите количество дней: "))
    res = (dt.today() + td(days = n))
    print(
        f"Через {n} дней будет {res.date()}.\nДень недели - {res.isoweekday()}"
    )

if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/43852dd97c5b4bcc1935e9d53dab4b3f567486f0/img/screenshot_4_9.png)
## Выводы
краткие выводы

## Лабораторная работа №10
### 
```python
global result

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h

figure = input("1-прямоугольник, 2-треугольник: ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")
```
### Результат.
![Меню](https://github.com/aasoloveva/SoftwareEngineering/blob/43852dd97c5b4bcc1935e9d53dab4b3f567486f0/img/screenshot_4_10.png)
## Выводы
краткие выводы

## Самостоятельная работа №1
### 
```python
```
### Результат.
![Меню]()
## Выводы
развернутые выводы
  
## Самостоятельная работа №2
### 
```python
```
### Результат.
![Меню]()
## Выводы
развернутые выводы
  
## Самостоятельная работа №3
### 
```python
```
### Результат.
![Меню]()
## Выводы
развернутые выводы
  
## Самостоятельная работа №4
### 
```python
```
### Результат.
![Меню]()
## Выводы
развернутые выводы
  
## Самостоятельная работа №5
### 
```python
```
### Результат.
![Меню]()
## Выводы
развернутые выводы

## Общие выводы по теме
обшие выводы

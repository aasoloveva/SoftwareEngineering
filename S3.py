from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def checktriangle(a, b, c):
    if (a < b + c) and (b < a + c) and (c < a + b): return True
    else: return False

def minmaxtriangles(x, y, z):
    if checktriangle(max(x), max(y), max(z)):
        p = (max(x) + max(y) + max(z)) / 2
        print(f"Площадь треугольника из наибольших элементов: {sqrt(p * (p - max(x)) * (p - max(y)) * (p - max(z)))}")
    if checktriangle(min(x), min(y), min(z)):
        p = (min(x) + min(y) + min(z)) / 2
        print(f"Площадь треугольника из наименьших элементов: {sqrt(p * (p - min(x)) * (p - min(y)) * (p - min(z)))}")

if __name__ == "__main__":
    minmaxtriangles(one, two, three)
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
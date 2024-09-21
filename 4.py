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
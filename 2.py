x = int(input())
if x < 0:
    print("x < 0")
elif 0 < x < 10:
    print("x > 0 and x < 10")
elif x == 10 or x == 0:
    print("x = 10 or x = 0")
else:
    print("x > 10")

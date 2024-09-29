def smth(x, y):
    return x ** y

for i in range(3):
    for j in range(2, 5):
        print(i, "^", j, "=", smth(i, j))

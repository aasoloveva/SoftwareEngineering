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
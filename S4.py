one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def fixgrades(x):
    while x.count(2) != 0:
        x.remove(2)
    while x.count(3) != 0:
        tmp = x.index(3)
        x.remove(3)
        x.insert(tmp, 4)
    return x

print (fixgrades(one))
print (fixgrades(two))
print (fixgrades(three))
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
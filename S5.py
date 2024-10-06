list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def dothething(x):
    res = set()
    for i in x:
        res.add(i)
        if x.count(i) > 1:
            for j in range(x.count(i) - 1):
                res.add(str(i) * (j + 2))
    return res

print(dothething(list_1))
print(dothething(list_2))
print(dothething(list_3))
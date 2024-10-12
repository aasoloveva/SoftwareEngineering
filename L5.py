def sort_tuple(x):
    for i in x:
        if not isinstance(i, int):
            return x
    return tuple(sorted(x))


tupl1 = (5,5,3,1,9)
tupl2 = (5,5,2.1,'1',9)
print(sort_tuple(tupl1))
print(sort_tuple(tupl2))
def smth(tupl, id):
    try:
        first = tupl.index(id)
        try:
            second = tupl.index(id, first + 1)
            return tupl[first:second + 1]
        except ValueError:
            second = len(tupl) - 1
            return tupl[first:second + 1]
    except ValueError:
        return tuple()
print(smth((1,2,3),8))
print(smth((1,8,3,4,8,8,9,2),8))
print(smth((1,2,8,5,1,2,9),8))
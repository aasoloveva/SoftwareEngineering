arr = [1, 2, 3, 4, 5]
def swap(x):
    return list(x[-1::]) + x[1:-1:] + list(x[0:1:])
print(swap(arr))
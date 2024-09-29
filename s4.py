def mean(*args):
    res = 0
    for i in args:
        res += i
    print(res / len(args))

if __name__ == '__main__':
    mean(1, 2, 3, 4)
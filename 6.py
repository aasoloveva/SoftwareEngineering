def mean(num):
    return sum(num) / float(len(num))

def nums(**kwargs):
    for x, y in kwargs.items():
        print(f"{x} mean: {mean(y)}")

if __name__ == "__main__":
    nums(x=[1,2,3,4,5], y=[6,7,8], z=[9,10,11,12])
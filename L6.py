with open("input.txt", "a+") as f:
    f.write("\nLine 3")
with open ("input.txt", "r") as f:
    for l in f:
        print(l, end="")
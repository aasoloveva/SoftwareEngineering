h = int(input())
igolki = "^"
star = "*"
spaces = h - 1
width = 3
print(" " * spaces, "*", sep="")
for i in range(h - 1):
    spaces -= 1
    print(" " * spaces, end="")
    print(igolki * width)
    width += 2
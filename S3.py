pun = ".,?!:;\"'—()"
letters = 0
words = 0
lines = 0
with open("input3.txt", "r") as f:
    text = f.readlines()
for x in text:
    for y in pun:
        x = x.replace(y, "")
    words += len(x.split())
    for y in x.split():
        letters += len(y)
lines = len(text)
print(f"{letters} letters\n{words} words\n{lines} lines")
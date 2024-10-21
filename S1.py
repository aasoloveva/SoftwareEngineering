pun = ".,?!:;\"'—()"
with open("doc.txt", "r", encoding='Windows-1251') as f:
    text = f.readlines()
for x in text:
    for y in pun:
        if y == "-" or y == "—":
            x = x.replace(y, " ")
        else:
            x = x.replace(y, "")
    #print(x)
words = []
for x in text:
    words += x.split()
maxcount = 0
maxword = ""
for x in set(words):
    if words.count(x) > maxcount:
        maxcount = words.count(x)
        maxword = x
print(f"Количество слов: {len(words)}.")
print(f"Самое частое слово: {maxword}, встречающееся {maxcount} раз.")
prohibited = []
with open("input4.txt", "r") as f:
    prohibited += f.readline().split()
text = input()
textwopunct = text.lower()

for x in prohibited:
    while x in textwopunct:
        index = textwopunct.find(x)
        if index != -1:
            textwopunct = textwopunct[:index] + ("*" * len(x)) + textwopunct[index + len(x):]
            text = text[:index] + ("*" * len(x)) + text[index + len(x):]
print(text)
s = "Привет всем изучающим Python!"
sub = input()
print("Строка:", s)
for i in range(len(s)):
    if s[i] == sub:
        print("Буква есть в строке")
        break
else:
    print("Буквы в строке нету")
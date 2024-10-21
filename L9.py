def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        sought_words = [word for word in words if len(word) == max_length]

        if len(sought_words) == 1:
            return sought_words[0]

        return sought_words


print(longest_words('input.txt'))
print(longest_words('input2.txt'))
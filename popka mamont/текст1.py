def get_longest_words1(path):
    file = open(path, 'r')
    text = file.read()
    lines = text.split("\n")
    mx_len = 0
    longest_words = []
    for line in lines:
        words = line.split()
        for word in words:
            word_len = len(word)
            if word_len > mx_len:
                mx_len = word_len
                longest_words.clear()
                longest_words.append(word)
            elif word_len == mx_len:
                longest_words.append(word)
    file.close()
    if len(longest_words) == 1:
        return longest_words[0]
    else:
        return longest_words


def get_longest_words2(path):
    mx_len = 0
    longest_words = []
    with open(path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_len = len(word)
                if word_len > mx_len:
                    mx_len = word_len
                    longest_words.clear()
                    longest_words.append(word)
                elif word_len == mx_len:
                    longest_words.append(word)
    if len(longest_words) == 1:
        return longest_words[0]
    else:
        return longest_words






path = input("Укажите путь до файла")

print(get_longest_words2(path))
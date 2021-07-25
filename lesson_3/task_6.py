def int_func(phrase, onlyfirst=False):
    capital_letters = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
                       'i': 'I', 'j': 'J','k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P',
                       'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
                       'y': 'Y', 'z': 'Z'}
    words = phrase.split()
    capitalized_words = []
    final_string = ''

    if onlyfirst:
        for word_item in words:
            fl = word_item[:1]
            capitalized_words.append(capital_letters.get(fl) + word_item[1:])
    else:
        for word_item in words:
            new_word = ''
            for one_char in word_item:
                new_word += capital_letters.get(one_char)
            capitalized_words.append(new_word)

    final_string = " ".join(capitalized_words)
    return final_string

print(int_func('my text', True))
print(int_func('my text'))

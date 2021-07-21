s = input('Enter a couple words: ')
words = s.split(' ')

for i in words:
    print_str = i[:10] if len(i) > 10 else i
    print(str(words.index(i)+1) + ' ' + print_str)


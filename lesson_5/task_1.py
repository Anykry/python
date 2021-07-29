line = ' '
out_file = open("out_file.txt", "w")
while len(line) != 0:
    line = input('Enter string: ')
    if line == '':
        break
    out_file.writelines(line+'\n')
out_file.close()

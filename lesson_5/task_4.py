def str_replace(source_line):
    numbers = {'One': "Один", 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    return numbers.get(source_line[:source_line.find('-')-1]), source_line[source_line.find('-'):]


with open('task_4.txt', 'r', encoding='utf-8') as my_file:
    with open('task_4_result.txt', 'w', encoding='utf-8') as result_file:
        for line in my_file:
            rus, source = str_replace(line)
            result_file.writelines(str(rus) + str(source))

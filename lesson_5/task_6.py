def line_parser(line):
    my_course = line[:line.find(':')]
    course_time = 0
    numb = ''
    for i in line:

        if i.isdigit():
            numb += i
        else:
            course_time = course_time + int(numb) if len(numb) > 0 else course_time
            numb = ''

    return my_course, course_time


with open('task_6.txt', 'r', encoding='utf-8') as my_file:
    my_list = my_file.readlines()

course_dictionary = {}

for el in my_list:
    dict_key, dict_value = line_parser(el)
    course_dictionary.update({dict_key: dict_value})

print(course_dictionary)

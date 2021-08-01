from random import randint


with open('task_5.txt', 'w') as my_file:
    # генерируем список из 5-ти случайных элементов
    my_list = [str(randint(1, 300)) for el in range(5)]
    # разделяем элементы пробелами и скливаем в строку
    my_string = ' '.join(my_list)
    # пишем строку в файл
    my_file.write(my_string)

# читаем записанный файл в список
with open('task_5.txt', 'r') as my_file:
    read_string = my_file.read()
    read_list = read_string.split(' ')

    # преобразовываем список из строк в список из чисел и берем функцию суммы от списка
    res = sum([int(my_item) for my_item in read_list])

    print(res)

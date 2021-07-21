#наполняем список произвольным количеством элементов, пока не будет введен -1
val = ''
list_a = []
while val != '-1':
    val = input('Enter list item. For finish enter -1: ')
    if val != '-1':
        list_a.append(val)

print(list_a)
print('Total items: '+str(len(list_a)))

#Проверяем, что в списке четное кол-во элементов, если нет - вырезаем последний элемент, превращая в четное кол-во элементов
last_item = None
if len(list_a)%2 != 0:
    last_item = list_a.pop(-1)

#меняем местами элементы в списке
list_a[::2], list_a[1::2] = list_a[1::2], list_a[::2]

#Если было нечетное кол-во элементов возвращаем на место последний элемент
if last_item is not None:
    list_a.append(last_item)

print(list_a)

from random import randint

my_list = [randint(1,300) for el in range(5)]
new_list = []

print(my_list)
for i in range(len(my_list)):
    if i == 0:
        continue
    if my_list[i] > my_list[i-1]:
        new_list.append(my_list[i])

print(new_list)


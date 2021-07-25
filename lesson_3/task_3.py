def my_func(a, b, c):
    val_list = []
    val_list.append(a)
    val_list.append(b)
    val_list.append(c)

    val_list.sort(reverse = True)

    return val_list[0] + val_list[1]

print(my_func(5,2,3))

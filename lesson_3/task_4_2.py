def my_func(x, y):
    result = 1
    k = 1
    while k <= abs(y):
        result = result * 1/x
        k += 1

    return result

print('Result = ' + str(my_func(3,-2)))

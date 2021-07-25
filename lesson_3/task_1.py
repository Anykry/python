def func_div(a, b):
    try:
        result = a / b
    except Exception:
        result = None

    return result

a = float(input('Enter the number a: '))
b = float(input('Enter the number b: '))

print('The resut of a/b is: '+str(func_div(a, b)))

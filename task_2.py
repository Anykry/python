class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


a = float(input('Enter a:'))
b = float(input('Enter b:'))

try:
    if b == 0:
        raise MyException('You try divide by zero')
except MyException as err:
    print(err)
else:
    res = a / b
    print(res)

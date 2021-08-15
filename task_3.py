class CheckValue(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    entered_value = input('Enter your value:')
    if entered_value == 'stop':
        break
    try:
        if not entered_value.isdigit():
            raise CheckValue('Entered value is not an integer')
    except CheckValue as err:
        print(err)
    else:
        my_list.append(entered_value)

print(my_list)

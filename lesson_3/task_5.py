def getsum_of_array(array_of_numbers):
    return sum(array_of_numbers)

def str_to_int(str_array):
    int_array = []
    for i in str_array:
        int_array.append(int(i))
    return int_array

input_lines = True
sum_of_array = 0
while input_lines:
    entered_line = input('Enter numbers separated by space. When you finish enter !: ')
    sign = entered_line.find('!')
    if sign == -1:
        symb_array = str_to_int(entered_line.split())
        sum_of_array += getsum_of_array(symb_array)
    else:
        input_lines = False
        symb_array = str_to_int(entered_line[:sign-1].split())
        sum_of_array += getsum_of_array(symb_array)

    print(f"The sum of entered numbers is: {sum_of_array}")

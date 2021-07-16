# --------------TASK 1--------------

a = 17
b = 23
c = int(input('Task 1. Operations with variables. Enter c variable: '))

d = a + b + c

result = f"a + b + c = {a} + {b} + {c} = {d}"

print(result)

# --------------TASK 2--------------

time_in_sec = int(input('Task 2. Format time in seconds to hh:mm:ss. Enter time in seconds: '))
time_hour = time_in_sec / 3600

# --------------TASK 3--------------

first_digit = int(input('Task 3. String<->Integer types. Enter any int number: '))
second_digit = int(str(first_digit) + str(first_digit))
third_digit = int(str(first_digit) + str(first_digit) + str(first_digit))
sum_ = first_digit + second_digit + third_digit

print('The sum of n + nn + nnn is: ' + str(sum_))

# --------------TASK 4--------------

number = input("Task 4. Founding max value. Loops. Enter int number: ")

max = 0
i = 0
max_is_found = False
max_itterations = len(number)

while not max_is_found:
    i += 1
    for symbol in number:
        symb_int = int(symbol)
        if symb_int >= max:
            max = symb_int
    if i == max_itterations + 1:
        max_is_found = True
print('Max digit is: '+str(max))

# --------------TASK 5--------------
print('Task 6. Profit&Loss')
profit = float(input('Enter company income: '))
loss = float(input('Enter company loss: '))

if profit >= loss:
    print('A Company has profit :)')
    profitability = profit / loss
    employees = int(input('Enter qantity of employees of a Company: '))
    profit_on_employee = profitability / employees

    print('The profitability on one employee is: '+str(profit_on_employee))
else:
    print('A company has a loss :(')

# --------------TASK 6--------------
a = int(input("Task 6. Sport's measurement. Enter first day result: "))
b = int(input('Enter your goal: '))
current_result = a
day = 1
while current_result < b:
    current_result = current_result * 1.1
    day += 1

print(f"You need {day} days for your goal!")

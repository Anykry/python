def employee_data(line):
    line = line.replace('\n', '')
    str_data = line.partition(' ')
    return str_data[0], str_data[2]


salary_file = open('task_3_salary.txt', 'r', encoding='utf-8')

sum_salary = 0

lines_array = salary_file.readlines()
for employee in lines_array:
    last_name, salary = employee_data(employee)
    if float(salary) < 20000:
        print(last_name, salary)
    sum_salary += float(salary)

print(f'The average salary from file is: {sum_salary / len(lines_array)}')

salary_file.close()

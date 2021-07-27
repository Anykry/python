from sys import argv

script_name, job, rate, bonus = argv
salary = (float(job) * float(rate)) + float(bonus)

print(f'The salary is: {salary}')
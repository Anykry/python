my_file = open('task_1_out_file.txt', "r")
total_lines = my_file.readlines()

print(f'In this file: {len(total_lines)} lines')

for el, line in enumerate(total_lines):
    print(f'In line {el+1} - {line.count(" ")+1} words')

my_file.close()

import itertools

start = int(input('Enter start number: '))
end = int(input('Enter the end number: '))

my_list = []

for el in itertools.count(start):
    my_list.append(el)
    if el == end:
        break

print(f'Created the list: {my_list}')

repeat_count = int(input('Enter times to repeat the list: '))

iterated_list = itertools.cycle(my_list)
i = 1
while i <= repeat_count:
    print(f'{i} - {next(iterated_list)}')
    i += 1

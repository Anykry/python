val = 0
list_a = []
while val != -1:
    val = int(input('Enter rate. For finish enter -1: '))
    if val == -1:
        break
    k = 0
    inserted = False
    for i in list_a:
        if val >= i:
            list_a.insert(k, val)
            inserted = True
            break
        k += 1
    if not inserted:
        list_a.append(val)
    print(list_a)

print(list_a)

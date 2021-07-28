def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial


n = fact(4)

for el in n:
    print(el)

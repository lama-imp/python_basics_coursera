my_range = range(10)
print(tuple(my_range))

for x in ('red', 'green', 'black'):
    print(x, 'apple')

for i in range(1, 30, 2):
    print(i, end=' ')

for i in range(10, -1, -1):
    print(i, end=' ')

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=' ')
    print()

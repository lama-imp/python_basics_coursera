
n = int(input())
# n = 3
for i in range(1, n + 1):
    print('+___', end=' ')
print()
for i in range(1, n + 1):
    print('|', i, ' /', sep='', end=' ')
print()
for i in range(1, n + 1):
    print('|__\ ', end='')
print()
for i in range(1, n + 1):
    print('|   ', end=' ')

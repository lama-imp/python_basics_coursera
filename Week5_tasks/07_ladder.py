n = int(input())
for i in range(1, n + 1):
    res = range(1, i + 1)
    print(*tuple(res), sep='')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a != 0:
    x = -b // a
else:
    x = b
if c * x + d == 0:
    print('NO')
elif a == 0 and b == 0:
    print('INF')
elif a * x + b == 0:
    print(x)
else:
    print('NO')

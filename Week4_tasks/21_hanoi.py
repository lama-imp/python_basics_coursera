def han(n, x, y):
    z = 6 - x - y
    if n == 1:
        print(n, x, y)
    else:
        han(n - 1, x, z)
        print(n, x, y)
        han(n - 1, z, y)


x, y = 1, 3
n = int(input())
han(n, x, y)

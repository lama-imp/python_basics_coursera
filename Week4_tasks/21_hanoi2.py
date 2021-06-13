def han(n, x, y):
    if x == -3 or x == 4:
        x = 1
    elif x == -2 or x == 5:
        x = 2
    elif x == -1 or x == 6:
        x = 3

    if y == -3 or y == 4:
        y = 1
    elif y == -2 or y == 5:
        y = 2
    elif y == -1 or y == 6:
        y = 3

    if n == 1:
        return n, x, y
    else:
        return han(n - 1, x, y - 1)
        print(n, x, y)
        return han(n - 1, x + 1, y)


x, y = 1, 3
n = int(input())
han(n, x, y)

def power(a, n):
    x = 0
    b = 1
    if n < 0:
        while x > n:
            b /= a
            x -= 1
    else:
        while x < n:
            b *= a
            x += 1
    return b


a, n = float(input()), int(input())
print(power(a, n))

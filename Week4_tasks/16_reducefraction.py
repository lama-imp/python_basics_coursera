def gcd(a, b):
    if a > b:
        a, b = a, b
    else:
        a, b = b, a
    if a % b != 0:
        return gcd(b, a % b)
    else:
        return b


def reduce_fraction(n, m):
    a = gcd(n, m)
    if a == 1:
        return int(n), int(m)
    else:
        return reduce_fraction(n / a, m / a)


n, m = int(input()), int(input())
print(*reduce_fraction(n, m))

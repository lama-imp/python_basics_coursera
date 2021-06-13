from math import sqrt


def lagrange1(n):
    if n % sqrt(n) == 0:
        return str(int(sqrt(n)))
    else:
        x = int(sqrt(n))
        return str(x) + ' ' + lagrange1(n - x ** 2)


def lagrange2(n):
    if n % sqrt(n) == 0:
        return str(int(sqrt(n)))
    else:
        x = int(sqrt(n)) - 1
        return str(x) + ' ' + lagrange1(n - x ** 2)


# n = int(input())
n = 7168
a = lagrange1(n)
b = lagrange2(n)

print(a.count(' '))
print(a, '/', b)
if a.count(' ') > 3:
    print(b)
else:
    print(a)

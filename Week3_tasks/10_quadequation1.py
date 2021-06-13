from math import sqrt
a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    if x2 > x1:
        print(x1, x2)
    else:
        print(x2, x1)
elif d == 0:
    print((-b) / (2 * a))

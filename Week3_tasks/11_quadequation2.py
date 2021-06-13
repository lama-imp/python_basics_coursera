from math import sqrt
a = float(input())
b = float(input())
c = float(input())

d = b ** 2 - 4 * a * c

if a != 0:
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        if x2 > x1:
            print(2, x1, x2)
        else:
            print(2, x2, x1)
    elif d == 0:
        print(1, (-b) / (2 * a))
    elif d < 0:
        print(0)

elif b != 0:
    print(1, -c / b)
else:
    if c != 0:
        print(0)
    else:
        print(3)

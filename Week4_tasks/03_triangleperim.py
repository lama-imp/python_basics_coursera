from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
a = distance(x1, y1, x2, y2)
b = distance(x2, y2, x3, y3)
c = distance(x1, y1, x3, y3)

print(a + b + c)

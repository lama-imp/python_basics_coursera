from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def is_point_in_circle(x, y, xc, yc, r):
    return distance(x, y, xc, yc) <= r


x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())

if is_point_in_circle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')

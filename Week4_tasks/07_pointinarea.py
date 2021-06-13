from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def is_point_in_circle(x, y, xc, yc, r):
    return distance(x, y, xc, yc) <= r


def is_point_not_in_circle(x, y, xc, yc, r):
    return distance(x, y, xc, yc) >= r


def is_point_in_area(x, y):
    a = is_point_in_circle(x, y, xc, yc, r)
    b = is_point_not_in_circle(x, y, xc, yc, r)
    first_left = y <= -x and x <= -y
    first_right = y >= -x and x >= -y
    second_left = y >= 2 * x + 2 and x <= 0.5 * y - 1
    second_right = y <= 2 * x + 2 and x >= 0.5 * y - 1
    up = a and first_right and second_left
    down = b and first_left and second_right
    return up or down


xc, yc, r = -1, 1, 2
x, y = float(input()), float(input())

if is_point_in_area(x, y):
    print('YES')
else:
    print('NO')

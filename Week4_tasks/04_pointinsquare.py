def is_point_in_square(x, y):
    return abs(x) <= 1 and abs(y) <= 1


x, y = float(input()), float(input())
if is_point_in_square(x, y):
    print('YES')
else:
    print('NO')

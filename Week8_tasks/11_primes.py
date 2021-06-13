from math import sqrt

print(2, *filter(
    lambda y: not any(map(lambda x: y % x == 0, range(2, int(sqrt(y) + 2)))),
    range(3, int(input()) + 1)
))

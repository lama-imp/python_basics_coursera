x = float(input())
y = float(input())
print(x + y)

if 0.1 + 0.2 == 0.3:
    print('yes')
else:
    print('no')

print('{0:.25f}'.format(0.1))  # количество знаков после запятой

print(500.0.as_integer_ratio())

print(11 % 2.5)

# Код для сравнения двух чисел, заданных с точностью 6 знаков после точки, выглядит так:

x = float(input())
y = float(input())
epsilon = 10 ** -6
if abs(x - y) < epsilon:
    print('Equal')
else:
    print('Not equal')

from math import floor, ceil  # названия функций * все функции

# import math

print(int(2.5), int(3.5), int(-2.5))
print(floor(2.5), floor(3.5), floor(-2.5))
print(ceil(2.5), ceil(3.5), ceil(-2.5))
print(round(2.5), round(3.5), round(-2.5))

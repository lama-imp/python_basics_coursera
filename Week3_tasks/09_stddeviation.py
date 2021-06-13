from math import sqrt

x = int(input())
n = 0
s_x = 0
s_x2 = 0

while x != 0:
    s_x += x
    s_x2 += x ** 2
    n += 1
    # print('sum sq =', s_x2, 'sum=', s_x, 'n=', n)
    x = int(input())

a = s_x2
b = s_x ** 2
c = b / n
d = a - c
e = d / (n - 1)
f = sqrt(e)
print(f)

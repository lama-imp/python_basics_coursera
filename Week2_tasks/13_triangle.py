a = int(input())
b = int(input())
c = int(input())
if a >= b:
    if b >= c or a > c:
        hy = a
    else:
        hy = c
elif b >= c:
    hy = b
else:
    hy = c
if a <= 0 or b <= 0 or c <= 0:
    print('impossible')
elif hy == a:
    if a ** 2 == b ** 2 + c ** 2:
        print('rectangular')
    elif a >= b + c:
        print('impossible')
    elif a ** 2 > b ** 2 + c ** 2:
        print('obtuse')
    elif a ** 2 < b ** 2 + c ** 2:
        print('acute')
elif hy == b:
    if b ** 2 == a ** 2 + c ** 2:
        print('rectangular')
    elif b >= a + c:
        print('impossible')
    elif b ** 2 > a ** 2 + c ** 2:
        print('obtuse')
    elif b ** 2 < a ** 2 + c ** 2:
        print('acute')
elif hy == c:
    if c ** 2 == b ** 2 + a ** 2:
        print('rectangular')
    elif c >= b + a:
        print('impossible')
    elif c ** 2 > a ** 2 + b ** 2:
        print('obtuse')
    elif c ** 2 < b ** 2 + a ** 2:
        print('acute')
else:
    print('impossible')

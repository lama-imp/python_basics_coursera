a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if a >= b:
    if b >= c or a > c:
        max = a
    else:
        max = c
elif b >= c:
    max = b
else:
    max = c
if d >= e:
    if max == a:
        if b <= d and c <= e:
            print('YES')
        elif c <= d and b <= e:
            print('YES')
        else:
            print('NO')
    elif max == b:
        if a <= d and c <= e:
            print('YES')
        elif c <= d and a <= e:
            print('YES')
        else:
            print('NO')
    elif max == c:
        if b <= d and a <= e:
            print('YES')
        elif a <= d and b <= e:
            print('YES')
        else:
            print('NO')
elif e > d:
    if max == a:
        if b <= e and c <= d:
            print('YES')
        elif c <= e and b <= d:
            print('YES')
        else:
            print('NO')
    elif max == b:
        if a <= e and c <= d:
            print('YES')
        elif c <= e and a <= d:
            print('YES')
        else:
            print('NO')
    elif max == c:
        if b <= e and a <= d:
            print('YES')
        elif a <= e and b <= d:
            print('YES')
        else:
            print('NO')

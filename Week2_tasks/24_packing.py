l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())
hi = h1 + h2
v1 = l1 + l2
v2 = w1 + w2
v3 = l1 + w2
v4 = w1 + l2
z = 1
if h1 > hc or h2 > hc:
    z = 0
elif l1 > lc and l1 > wc:
    z = 0
elif w1 > wc and w1 > lc:
    z = 0
elif l2 > lc and l2 > wc:
    z = 0
elif w2 > wc and w2 > lc:
    z = 0
if z == 0:
    print('NO')
elif v1 <= lc and w1 <= wc and w2 <= wc:
    print('YES')
elif v2 <= lc and l1 <= wc and l2 <= wc:
    print('YES')
elif v3 <= lc and w1 <= wc and l2 <= wc:
    print('YES')
elif v4 <= lc and l1 <= wc and w2 <= wc:
    print('YES')
elif v1 <= wc and w1 <= lc and w2 <= lc:
    print('YES')
elif v2 <= wc and l1 <= lc and l2 <= lc:
    print('YES')
elif v3 <= wc and w1 <= lc and l2 <= lc:
    print('YES')
elif v4 <= wc and l1 <= lc and w2 <= lc:
    print('YES')
elif hi <= hc:
    if l1 <= lc and w1 <= wc:
        if w2 <= wc and l2 <= lc:
            print('YES')
        elif w2 <= lc and l2 <= wc:
            print('YES')
    elif l1 <= wc and w1 <= lc:
        if w2 <= wc and l2 <= lc:
            print('YES')
        elif w2 <= lc and l2 <= wc:
            print('YES')
else:
    print('NO')

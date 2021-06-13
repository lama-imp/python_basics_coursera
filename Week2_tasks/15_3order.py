a, b, c = int(input()), int(input()), int(input())
# a, b, c = 1, -3, 2
if a >= b:
    if b >= c:
        print(c, b, a)
    elif b < c and a >= c:
        print(b, c, a)
    else:
        print(b, a, c)
elif b >= c:
    if c >= a:
        print(a, c, b)
    elif c < a and b >= a:
        print(c, a, b)
else:
    print(a, b, c)

def merge(a, b, c):
    if len(a) == 0:
        c.extend(b)
    elif len(b) == 0:
        c.extend(a)
    elif a[0] < b[0]:
        c.append(a[0])
        d = a[1:]
        merge(d, b, c)
    else:
        c.append(b[0])
        d = b[1:]
        merge(a, d, c)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
merge(a, b, c)
print(*c)

def same(a, b):
    c = []
    if len(a) < len(b):
        for i in a:
            if b.count(i) > 0:
                c.append(i)
    else:
        for i in b:
            if a.count(i) > 0:
                c.append(i)
    print(*c)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
same(a, b)

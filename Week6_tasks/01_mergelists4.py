def merge(a, b):
    count_a = 0
    count_b = 0
    c = []
    while True:
        if len(a) == count_a:
            c.extend(b[count_b:])
            break
        elif len(b) == count_b:
            c.extend(a[count_a:])
            break
        elif a[count_a] < b[count_b]:
            c.append(a[count_a])
            count_a += 1
        else:
            c.append(b[count_b])
            count_b += 1
    print(*c)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
merge(a, b)

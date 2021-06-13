def same(a, b):
    count_a = 0
    count_b = 0
    c = []
    while True:
        if len(a) == count_a:
            break
        elif len(b) == count_b:
            break
        elif a[count_a] == b[count_b]:
            c.append(a[count_a])
            count_a += 1
            count_b += 1

        elif a[count_a] < b[count_b]:
            count_a += 1
        else:
            count_b += 1
    print(*c)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
same(a, b)

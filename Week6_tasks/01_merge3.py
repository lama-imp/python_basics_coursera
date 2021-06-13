def merge(a, b):
    if a[0] <= b[0]:
        c = a + b
        count = 0
        while count < len(c):
            count += 1
            for i in range(len(c)):
                if i > 0:
                    if c[i] < c[i - 1]:
                        temp = c[i]
                        c[i] = c[i - 1]
                        c[i - 1] = temp
    else:
        c = b + a
        count = 0
        while count < len(c):
            count += 1
            for i in range(len(c)):
                if i > 0:
                    if c[i] < c[i - 1]:
                        temp = c[i]
                        c[i] = c[i - 1]
                        c[i - 1] = temp
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*merge(a, b))

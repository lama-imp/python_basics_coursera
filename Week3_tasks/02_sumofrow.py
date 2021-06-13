n = float(input())
a = 1
c = 0
while a <= n:
    b = (1 / (a ** 2))
    c += b
    a += 1
    # print(a, b, c)

print(c)

k = int(input())
count = 0
n = 1
while n <= k:
    m = n
    c = str()
    while m > 0:
        a = m % 10
        m = m // 10
        b = str(a)
        c += b
        # if count2 == 0:
        #     d = c
        # else:
        #     d = c + a
        # count2 += 1
        # print(n, a, d, m)
        # print(m)
    # print(n, c)
    if int(c) == n:
        count += 1
    n += 1

print(count)

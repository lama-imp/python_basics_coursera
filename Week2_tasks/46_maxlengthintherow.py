n = int(input())
prev = 0
total = 0
while n != 0:
    # prev = n
    # n = int(input())
    count_i = 1
    count_d = 1
    if prev == 0 or n == prev:
        prev = n
        n = int(input())
    while n > prev and n != 0:
        # print(n, prev)
        count_i += 1
        # print('i', count_i)
        prev = n
        n = int(input())

    while n < prev and n != 0:
        # print(n, prev)
        count_d += 1
        # print('d', count_d)
        prev = n
        n = int(input())

    if count_i > count_d:
        count = count_i
    else:
        count = count_d
    if total > count:
        total = total
    else:
        total = count
print(total)

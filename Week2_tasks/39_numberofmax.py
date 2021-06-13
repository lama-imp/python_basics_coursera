now = int(input())
max = 0
n = 1
while now != 0:
    if now >= max:
        if now > max:
            n = 1
        if now == max:
            n += 1
        max = now
    now = int(input())
print(n)

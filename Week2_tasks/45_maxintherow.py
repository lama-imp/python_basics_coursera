n = int(input())
prev = 0
total = 0
while n != 0:
    prev = n
    n = int(input())
    count = 1
    while n == prev and n != 0:
        count += 1
        n = int(input())
    if total > count:
        total = total
    else:
        total = count
print(total)

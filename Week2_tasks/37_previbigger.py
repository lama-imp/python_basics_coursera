num = int(input())
first = 0
second = 0
n = -1
while num != 0:
    first = second
    # print(first)
    second = num
    # print(second)
    if second > first:
        n += 1
    num = int(input())
print(n)

now = int(input())
# if now % 2 == 0:
#     n = 1
# else:
#     n = 0
n = 0
while now != 0:
    if now % 2 == 0:
        n += 1
    now = int(input())
print(n)

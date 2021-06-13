list = list(map(int, input().split()))
idx = 0
for i, x in enumerate(list):
    if i == 0:
        num = x
    if x > num:
        num = x
        idx = i
print(num, idx)

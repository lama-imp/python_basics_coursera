list = list(map(int, input().split()))
max1 = max(list)
min1 = min(list)
temp = list.copy()
max_idx = list.index(max1)
min_idx = list.index(min1)
if max_idx > min_idx:
    temp.pop(max_idx)
    temp.pop(min_idx)
else:
    temp.pop(min_idx)
    temp.pop(max_idx)

max2 = max(temp)
min2 = min(temp)

if max1 * max2 > min1 * min2:
    print(max2, max1)
else:
    print(min1, min2)

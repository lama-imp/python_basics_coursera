list = list(map(int, input().split()))
if len(list) > 4:
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
    max_idx2 = temp.index(max2)
    min_idx2 = temp.index(min2)
    if max_idx2 > min_idx2:
        temp.pop(max_idx2)
        temp.pop(min_idx2)
    else:
        temp.pop(min_idx2)
        temp.pop(max_idx2)

    max3 = max(temp)
    min3 = min(temp)

    if max1 * max2 * max3 > min1 * min2 * max1:
        print(max3, max2, max1)
    else:
        print(min1, min2, max1)
elif len(list) > 3:
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
    if max1 * max2 * min2 > min1 * min2 * max1:
        print(min2, max2, max1)
    else:
        print(min1, min2, max1)
else:
    print(*list)

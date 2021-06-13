list = list(map(int, input().split()))
count = 0
for i, x in enumerate(list):
    if i > 0 and i < len(list) - 1:
        if x > list[i - 1] and x > list[i + 1]:
            count += 1
print(count)

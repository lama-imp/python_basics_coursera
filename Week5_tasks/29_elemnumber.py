list = list(map(int, input().split()))
count = 1
for i, x in enumerate(list[:-1]):
    if x != list[i + 1]:
        count += 1
print(count)

list = list(map(int, input().split()))
count = 0
for i, x in enumerate(list):
    slice = list[i + 1:]
    if slice.count(x) > 0:
        count += slice.count(x)
print(count)

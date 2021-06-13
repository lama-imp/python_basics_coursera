list = list(map(int, input().split()))
for i, x in enumerate(list):
    if i == 0:
        continue
    if x > 0 and list[i - 1] > 0:
        print(*list[i - 1:i + 1])
        break
    if x < 0 and list[i - 1] < 0:
        print(*list[i - 1:i + 1])
        break

list = list(map(int, input().split()))

for i in range(len(list) - 1, -1, -1):
    if list[i] == 0:
        list.pop(i)
        list.append(0)

print(*list)

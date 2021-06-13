list = list(map(int, input().split()))
fr = 0
to = -1
for i, x in enumerate(list):
    if i < len(list) / 2:
        a = list[to]
        list[to] = list[fr]
        list[fr] = a
        to -= 1
        fr += 1
print(*list)

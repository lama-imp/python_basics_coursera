nlist = list(map(int, input().split()))
idx = int(input())

for i, x in enumerate(nlist):
    if i >= idx and i + 1 < len(nlist):
        nlist[i] = nlist[i + 1]
nlist.pop()
print(*nlist)

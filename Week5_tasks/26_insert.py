nlist = list(map(int, input().split()))
temp = list(map(int, input().split()))
idx = temp[0]
num = temp[1]
nlist.append(num)
for i in range(len(nlist) - 1, -1, -1):
    if i > idx:
        nlist[i] = nlist[i - 1]
    elif i == idx:
        nlist[i] = num
print(*nlist)

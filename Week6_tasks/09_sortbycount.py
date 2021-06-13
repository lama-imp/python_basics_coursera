lst = list(map(int, input().split()))
temp = [0] * 101
for i in lst:
    temp[i] += 1

for i in range(len(temp)):
    print(temp[i] * (str(i) + ' '), end='')

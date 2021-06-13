s = []
row = []
line = []
check = 0

for i in range(8):
    i = list(map(int, input().split()))
    s.append(i)
    row.append(i[0])
    line.append(i[1])

for i in row:
    if row.count(i) > 1:
        check += 1
for i in line:
    if line.count(i) > 1:
        check += 1

for i in s:
    x = i[0]
    y = i[1]
    c = y - x
    d = x + y
    for j in range(8):
        if s[j][0] - s[j][1] + c == 0 or d - s[j][0] - s[j][1] == 0:
            if s[j][0] == x and s[j][1] == y:
                continue
            else:
                check += 1

if check == 0:
    print('NO')
else:
    print('YES')

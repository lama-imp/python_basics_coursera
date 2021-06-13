fin = open('input.txt', 'r', encoding='utf8')
n = int(fin.readline())
possible = set()
inset = set()
notinset = set()
prev_line = []
check = 0
for i in range(1, n + 1):
    possible.add(i)
for line in fin:
    line = line.strip()
    if line == 'HELP':
        break
    elif line == 'YES' or line == 'NO':
        if line == 'YES':
            temp = set()
            if len(prev_line) == 1:
                check = 1
                answer = prev_line
                break
            elif len(inset) == 0:
                for i in prev_line:
                    inset.add(i)
            else:
                for i in prev_line:
                    temp.add(i)
                todel = inset - temp
                inset -= todel
        else:
            for i in prev_line:
                notinset.add(i)
    else:
        prev_line = list(map(int, line.split()))
if check != 1:
    if len(inset) == 0:
        print(*sorted(possible - notinset))
    else:
        print(*sorted((possible & inset) - notinset))
else:
    print(*prev_line)

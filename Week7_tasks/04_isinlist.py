inlist = list(map(int, input().split()))
listset = set()
for i in inlist:
    if i in listset:
        print('YES')
    else:
        print('NO')
        listset.add(i)

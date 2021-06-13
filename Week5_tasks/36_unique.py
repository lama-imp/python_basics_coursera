list = list(map(int, input().split()))
for i in list:
    if list.count(i) == 1:
        print(i, end=' ')

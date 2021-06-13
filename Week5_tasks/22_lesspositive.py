list = list(map(int, input().split()))
check = 1000
for i in list:
    if i > 0 and i < check:
        check = i
print(check)

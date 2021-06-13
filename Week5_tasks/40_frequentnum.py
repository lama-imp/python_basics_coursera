list = list(map(int, input().split()))
count = 0
num = 0
for i in list:
    if list.count(i) > count:
        count = list.count(i)
        num = i
print(num)

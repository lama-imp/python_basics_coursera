my_list = list(map(int, input().split()))
count = 0
for i in my_list:
    if i > 0:
        count += 1
print(count)

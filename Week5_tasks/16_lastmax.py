my_list = list(map(int, input().split()))
c = int(max(my_list))

for idx, num in enumerate(my_list):
    if num == c:
        pos = idx
print(c, pos)

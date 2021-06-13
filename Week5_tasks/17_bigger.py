my_list = list(map(int, input().split()))
fin_list = []
for idx, i in enumerate(my_list):
    if idx != 0:
        if my_list[idx - 1] < i:
            fin_list.append(i)
print(*fin_list)

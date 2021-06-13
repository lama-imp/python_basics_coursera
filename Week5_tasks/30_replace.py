in_list = list(map(int, input().split()))
out_list = []
for i, x in enumerate(in_list):
    if i % 2 != 0:
        out_list.append(x)
        out_list.append(in_list[i - 1])
    elif i % 2 == 0 and i == len(in_list) - 1:
        out_list.append(x)

print(*out_list)

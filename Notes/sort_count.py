lst = list(map(int, input().split()))
# new_list = []
# for i in range(len(lst)):
#     new_list.append((lst[i], i))
# new_list.sort()
# print(new_list)
# for now in new_list:
#     print(now[1], end=' ')
grades = [0] * 11
for now in lst:
    grades[now] += 1
for grade in range(len(grades)):
    print((str(grade) + ' ') * grades[grade], end=' ')

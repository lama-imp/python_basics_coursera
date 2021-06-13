#  В списке все элементы попарно различны. Поменяйте местами минимальный \
# и максимальный элемент этого списка.
list = list(map(int, input().split()))
max = int(max(list))
min = int(min(list))
max_idx = list.index(max)
min_idx = list.index(min)
list[max_idx] = min
list[min_idx] = max
print(*list)

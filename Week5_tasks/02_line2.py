a, b = int(input()), int(input())
if a < b:
    my_range = range(a, b + 1)
else:
    my_range = range(a, b - 1, -1)
print(*tuple(my_range))

from math import floor, ceil
n = float(input())
a = n - int(n)

if a >= 0.5:
    answer = ceil(n)
elif a < 0.5:
    answer = floor(n)
print(answer)

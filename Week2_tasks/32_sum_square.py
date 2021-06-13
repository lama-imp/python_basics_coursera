now = int(input())
# now = 3
n = 1
sum_sq = 0
while n <= now:
    n_sq = n ** 2
    sum_sq += n_sq
    n += 1
    # print(n_sq, sum_sq)
print(sum_sq)

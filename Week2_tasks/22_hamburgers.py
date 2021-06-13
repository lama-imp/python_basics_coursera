k, m, n = int(input()), int(input()), int(input())
s = n * 2
p = (s + k - 1) // k
if n <= k:
    print(m * 2)
else:
    print(m * p)

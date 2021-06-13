n = int(input())
m = int(input())
k = int(input())
# n = 10
# m = 2
# k = 7
if k == n or k == m:
    print('YES')
elif k % n == 0 and k <= n * m - n:
    print('YES')
elif k % m == 0 and k <= n * m - m:
    print('YES')
else:
    print('NO')

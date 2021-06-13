a = int(input())
# a = 13
f_n1 = 1
f_n2 = 0
n = 1
f_n = 1
while f_n < a:
    f_n = f_n1 + f_n2
    f_n2 = f_n1
    f_n1 = f_n
    n += 1
    # print(f_n, f_n1, f_n2, n)
if f_n == a:
    print(n)
else:
    print(-1)

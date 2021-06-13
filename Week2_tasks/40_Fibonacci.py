now = int(input())
# now = 3
f_n1 = 1
f_n2 = 0
n = 1
f_n = 1
while n != now:
    f_n = f_n1 + f_n2
    f_n2 = f_n1
    f_n1 = f_n
    n += 1
    # print(f_n, f_n1, f_n2, n)
print(f_n)

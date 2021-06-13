p = int(input())
x = int(input())
y = int(input())
k = int(input())

n = 0
sum_kop = x * 100 + y

while n < k:
    n += 1
    sum_1 = sum_kop + (sum_kop * p) // 100
    sum_kop = sum_1
    # print(n, 'after year=', sum_1, 'total=', sum_tot)

a = sum_1 // 100
b = sum_1 % 100

print(a, b, sep=' ')

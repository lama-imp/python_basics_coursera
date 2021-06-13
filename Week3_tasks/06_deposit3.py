p = int(input())
x = int(input())
y = int(input())

sum_kop = x * 100 + y
sum_1 = sum_kop + (sum_kop * p) // 100

a = sum_1 // 100
b = sum_1 % 100

print(a, b, sep=' ')

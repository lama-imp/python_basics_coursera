p = float(input())
x = float(input())
y = float(input())

pcnt = 1 + (p * (10 ** -2))
total = x + (y * (10 ** -2))
total_1 = total * pcnt
a = int(total_1)
b = int((total_1 - int(total_1)) * 100)

print('percent=', pcnt, 'total=', total, 'sum after=', total_1)
print(a, b, sep=' ')

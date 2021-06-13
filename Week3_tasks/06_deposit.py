p = float(input())
x = float(input())
y = float(input())

pcnt = 1 + (p * (10 ** -2))
x2 = x * pcnt  # deposit in rubles with percent
y2 = round((x2 - int(x2)) * 100)
y3 = round(y * pcnt)
if y3 + y2 >= 100:
    a = int(x2) + ((y + y2) // 100)
    b = int((y + y2) % 100)
else:
    a = int(x2)
    b = int((y + y2) % 100)

print('percent=', pcnt, 'deposit=', x2, )
print(a, b, sep=' ')

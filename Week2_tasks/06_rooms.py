x = int(input())
y = int(input())
# x = 50
# y = 100
if x == 1:
    print('YES')
elif (x - 1) % (y - x + 1) == 0:
    print('YES')
else:
    print('NO')

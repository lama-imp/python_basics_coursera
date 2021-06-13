a = int(input())
b = int(input())
c = int(input())
# a = 0
# b = -4
# c = -3
if a >= b:
    if b >= c or a > c:
        print(a)
    else:
        print(c)
elif b >= c:
    print(b)
else:
    print(c)

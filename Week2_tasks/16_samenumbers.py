a, b, c = int(input()), int(input()), int(input())
# a, b, c = 2, 2, 2
if a == b and b == c:
    print('3')
elif a == b or b == c or a == c:
    print('2')
else:
    print('0')

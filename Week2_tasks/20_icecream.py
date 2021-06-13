k = int(input())
# k = 2
if k % 5 == 0 or k % 3 == 0:
    print('YES')
elif (k % 5) % 3 == 0 or (k % 3) % 5 == 0:
    print('YES')
elif (k - 5) % 3 == 0 and k != 2:
    print('YES')
elif (k - 3) % 5 == 0:
    print('YES')
elif (k % 10) % 3 == 0:
    print('YES')
elif k > 10 and (k - 8) % 5 == 0:
    print('YES')
elif k > 10 and (k - 11) % 5 == 0:
    print('YES')
else:
    print('NO')

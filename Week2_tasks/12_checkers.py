start1 = int(input())
start2 = int(input())
end1 = int(input())
end2 = int(input())
# start1 = 1
# start2 = 1
# end1 = 2
# end2 = 2
h = end1 - start1
v = end2 - start2
if (start1 + end1) % 2 != 0 and (start2 + end2) % 2 != 0:
    colour = 1
elif (start1 + end1) % 2 == 0 and (start2 + end2) % 2 == 0:
    colour = 1
else:
    colour = 0
if colour == 0 or v <= 0:
    print('NO')
else:
    if v == 1 and h ** 2 == 1:
        print('YES')
    elif v == 2 and h ** 2 <= 4:
        print('YES')
    elif v >= 3:
        print('YES')
    else:
        print('NO')

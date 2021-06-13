start1 = int(input())
start2 = int(input())
end1 = int(input())
end2 = int(input())
# start1 = 1
# start2 = 1
# end1 = 1
# end2 = 2
if (start1 + end1) % 2 != 0 and (start2 + end2) % 2 != 0:
    print('YES')
elif (start1 + end1) % 2 == 0 and (start2 + end2) % 2 == 0:
    print('YES')
else:
    print('NO')

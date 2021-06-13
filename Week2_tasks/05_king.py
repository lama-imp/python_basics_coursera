start1 = int(input())
start2 = int(input())
end1 = int(input())
end2 = int(input())
# start1 = 2
# start2 = 4
# end1 = 7
# end2 = 6
if start1 == end1 or start1 == end1 - 1 or start1 == end1 + 1:
    a = 0
else:
    a = 1
if start2 == end2 or start2 == end2 - 1 or start2 == end2 + 1:
    b = 0
else:
    b = 1
if a == 0 and b == 0:
    print('YES')
else:
    print('NO')

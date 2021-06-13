# l1, r1 = int(input()), int(input())
# l2, r2 = int(input()), int(input())
# l3, r3 = int(input()), int(input())
l1, r1 = 7, 9
l2, r2 = 5, 12
l3, r3 = 15, 19
match1 = r1 - l1
match2 = r2 - l2
match3 = r3 - l3
if l1 > r2:
    gap12 = l1 - r2
else:
    gap12 = l2 - r1
if l2 > r3:
    gap23 = l2 - r3
else:
    gap23 = l3 - r2
if l1 > r3:
    gap13 = l1 - r3
else:
    gap13 = l3 - r1
# print(match2, gap13, gap12)
if gap12 <= 0 and (gap23 <= 0 or gap13 <= 0):
    if gap23 <= 0 or gap13 <= 0:
    answer = 0
elif match1 >= gap23:
    answer = 1
elif match2 >= gap13:
    answer = 2
elif match3 >= gap12:
    answer = 3
else:
    answer = -1
# a = match2 >= gap13
# print(a)
# print(gap12, gap23, gap13)
# print(match1, match2, match3)
print(answer)

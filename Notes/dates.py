start1 = int(input())
end1 = int(input())
start2 = int(input())
end2 = int(input())
# s1_in_2 = start2 <= start1 <= end2
# e1_in_2 = start2 <= end1 <= end2
# s2_in_1 = start1 <= start2 <= end1
# e2_in_1 = start1 <= end2 <= end1
answer = start1 <= end2 and start2 <= end1
print(answer)

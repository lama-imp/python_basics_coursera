now = int(input())
maxNum = 0
second_max = 0
while now != 0:
    if now != 0 and now > second_max:
        if now > maxNum:
            second_max = maxNum
            maxNum = now
        else:
            second_max = now
    now = int(input())
print(second_max)

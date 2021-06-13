key_number = int(input())
keys = list(map(int, input().split()))
push_number = int(input())
pushes = list(map(int, input().split()))
temp = [0] * key_number

for push in pushes:
    temp[push - 1] += 1
for i in range(key_number):
    if keys[i] < temp[i]:
        print('YES')
    else:
        print('NO')

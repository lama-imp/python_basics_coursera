village_number = int(input())
village_dist = list(map(int, input().split()))
shelter_number = int(input())
shelter_dist = list(map(int, input().split()))

villages = []
shelters = []
answer = [0] * village_number
for i, x in enumerate(village_dist):
    temp = (x, i)
    villages.append(temp)
for i, x in enumerate(shelter_dist):
    temp = (x, i)
    shelters.append(temp)
villages.sort()
shelters.sort()
count = 0
last_ans = 0
for village in villages:
    if count == 0:
        now = 10000000
        ans = 0
        for shelter in shelters:
            if abs(shelter[0] - village[0]) < now:
                now = abs(shelter[0] - village[0])
                ans = shelter[1]
        answer[village[1]] = ans
        last_ans = ans

    else:
        now = 10000000
        ans = 0
        for i in range(last_ans, len(shelters)):
            if abs(shelters[i][0] - village[0]) < now:
                now = abs(shelters[i][0] - village[0])
                ans = shelters[i][1]
        answer[village[1]] = ans
        last_ans = ans

for i in answer:
    print(i + 1, end=' ')

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
# print(villages, 'villages')
# print(shelters, 'shelters')

for village in villages:
    now = 1000000
    ans = 0
    for number, shelter in enumerate(shelters):
        # print(abs(shelter[0] - village[0]), now)
        if abs(shelter[0] - village[0]) < now:
            # print(shelter[0], village[0], abs(shelter[0] - village[0]))
            now = abs(shelter[0] - village[0])
            ans = shelter[1]
        # print(ans, 'ans')
        # elif abs(shelter[0] - village[0]) > now or number == len(shelters) - 1:
        #     answer.append(ans)
    answer[village[1]] = ans
    # answer.append(ans)
    # print(answer)

for i in answer:
    print(i + 1, end=' ')

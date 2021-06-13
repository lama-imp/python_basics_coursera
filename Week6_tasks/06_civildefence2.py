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
count = 1
for vil in villages:
    while count < shelter_number and (
        abs(vil[0] - shelters[count - 1][0]) > abs(vil[0] - shelters[count][0])
            ):
        count += 1
        # print(count)
    answer[vil[1]] = shelters[count - 1][1] + 1
print(*answer)

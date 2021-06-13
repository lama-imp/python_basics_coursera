fin = open('input.txt', 'r', encoding='utf8')
schools = [0] * 100
for line in fin:
    temp = list(line.split())
    schools[int(temp[2])] += 1
a = schools.count(max(schools))
answer = []
start = 0
counter = a
while counter > 0:
    answer.append(schools.index(max(schools), start))
    start = answer[-1] + 1
    counter -= 1
print(*answer)

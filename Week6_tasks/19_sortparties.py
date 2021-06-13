def sort_parties(party):
    return (-party[0], party[1])


fin = open('input.txt', 'r', encoding='utf8')
n = fin.readline()
parties = []
for line in fin:
    temp = line.strip()
    if temp == 'VOTES:':
        break
    else:
        parties.append(temp)

votes = [0] * len(parties)
for line in fin:
    a = parties.index(line.strip())
    votes[a] += 1

parties_sort = []
for i in range(len(parties)):
    temp = (votes[i], parties[i])
    parties_sort.append(temp)
parties_sort.sort(key=lambda x: -int(x[0]))
answer = []
for i in range(0, len(parties_sort), 2):
    if i < len(parties_sort) - 1:
        if parties_sort[i][0] != parties_sort[i + 1][0]:
            temp = parties_sort[i][1], parties_sort[i + 1][1]
            answer.extend(temp)
        else:
            temp = [parties_sort[i][1], parties_sort[i + 1][1]]
            temp.sort()
            answer.extend(temp)
    else:
        answer.append(parties_sort[i][1])
print(*answer, sep='\n')

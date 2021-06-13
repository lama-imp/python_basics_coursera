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
parties_sort.sort(key=sort_parties)

for party in parties_sort:
    print(party[1], sep='\n')

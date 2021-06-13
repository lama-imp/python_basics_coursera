fin = open('input.txt', 'r', encoding='utf8')
n = fin.readline()
parties = []
for line in fin:
    temp = line.strip()
    if temp == 'VOTES:':
        break
    else:
        parties.append(line)

votes = [0] * len(parties)
for line in fin:
    a = parties.index(line)
    votes[a] += 1
votes_number = sum(votes)
answer = []
for i in range(len(parties)):
    if votes[i] / votes_number >= 0.07:
        answer.append(parties[i])
print(*answer, sep='')

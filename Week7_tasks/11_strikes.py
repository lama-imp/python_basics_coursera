fin = open('input.txt', 'r', encoding='utf8')

n = list(map(int, fin.readline().split()))
days = range(1, n[0] + 1)
strikes = set()
for party in range(n[1]):
    line = list(map(int, fin.readline().split()))
    for day in range(line[0], n[0] + 1, line[1]):
        strikes.add(day)
weekends = set()
# for i in days[5::7]:
#     weekends.add(i)
for i in days[6::7]:
    weekends.add(i)
    weekends.add(i - 1)
if len(weekends) != 0 and n[0] - max(weekends) == 6:
    weekends.add(n[0])
# print(strikes, weekends)
print(len(strikes - weekends))

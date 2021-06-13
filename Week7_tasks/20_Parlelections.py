file = open('input.txt')
total_votes = 0
parties = dict()
for line in file:
    temp = line.split()
    parties[' '.join(temp[:-1])] = int(temp[-1])
    total_votes += int(temp[-1])
coeff = total_votes / 450
parties_seats = dict()
parties_decimals = []
total_seats = 0
for party in parties:
    parties_seats[party] = int(parties[party] // coeff)
    parties_decimals.append((
        parties[party] / coeff - parties[party] // coeff, party
    ))
    total_seats += parties_seats[party]
    parties_decimals.sort(reverse=True)

while total_seats < 450:
    if len(parties_decimals) > 1:
        for i in range(1, len(parties_decimals)):
            if parties_decimals[i - 1][0] > parties_decimals[i][0]:
                parties_seats[parties_decimals[i - 1][1]] += 1
                total_seats += 1
            elif parties_decimals[i - 1] == parties_decimals[i]:
                party1 = parties_decimals[i - 1][1]
                party2 = parties_decimals[i][1]
                if parties[party1] > parties[party2]:
                    parties_seats[party1] += 1
                    total_seats += 1
                else:
                    parties_seats[party2] += 1
                    total_seats += 1
            if total_seats == 450:
                break
    else:
        parties_seats[parties_decimals[0][1]] = 450
        total_seats = 450

for party in parties_seats:
    print(party, parties_seats[party])

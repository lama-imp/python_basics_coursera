file = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
candidates_dict = dict()
total_votes = 0
for line in file:
    candidates_dict[line.strip()] = candidates_dict.get(line.strip(), 0) + 1
    total_votes += 1
first = ''
first_votes = 0
second = ''
second_votes = 0
for candidate in candidates_dict:
    if candidates_dict[candidate] * 2 > total_votes:
        print(candidate, file=fout)
        fout.close()
        break
    else:
        if candidates_dict[candidate] > first_votes:
            second_votes = first_votes
            second = first
            first_votes = candidates_dict[candidate]
            first = candidate
        elif candidates_dict[candidate] > second_votes:
            second_votes = candidates_dict[candidate]
            second = candidate
else:
    print(first, file=fout)
    print(second, file=fout)
    fout.close()

file = open('input.txt')
results = dict()
for line in file:
    temp = line.split()
    results[temp[0]] = results.get(temp[0], 0) + int(temp[1])
for candidate in sorted(results):
    print(candidate, results[candidate])

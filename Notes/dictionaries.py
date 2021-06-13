capitals = {'Russia': 'Moscow', 'France': 'Paris'}
capitals['USA'] = 'Washington'
del capitals['France']
print(capitals)
print('Russia' in capitals)

my_dict = dict([('x', 5), ('y', 3)])
print(my_dict)
for i in my_dict:  # only keys
    print(i)
for i in my_dict:
    print(i, my_dict[i])

s = input()
letters = dict()
for char in s:
    if char in letters:
        letters[char] += 1
    else:
        letters[char] = 1
for char in s:
    if char not in letters:
        letters[char] = 0
    letters[char] += 1
for char in s:
    letters[char] = letters.get(char, 0) + 1
for char in sorted(letters):
    print(char, letters[char])

gas_cost = dict()
n = int(input())
a92, a95, a98 = map(int(input().split()))
gas_cost[92] = a92
gas_cost[95] = a95
gas_cost[98] = a98
for i in range(n - 1):
    a92, a95, a98 = map(int(input().split()))
    gas_cost[92] = a92
    gas_cost[95] = a95
    gas_cost[98] = a98

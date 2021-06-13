fin = open('input.txt', 'r', encoding='utf8')
cubes_number = list(map(int, fin.readline().split()))
anya_cubes_number = cubes_number[0]
borya_cubes_number = cubes_number[1]
anya_set = set()
borya_set = set()
for i in range(anya_cubes_number):
    anya_set.add(int(fin.readline()))
for i in range(borya_cubes_number):
    borya_set.add(int(fin.readline()))
print(len(anya_set & borya_set))
print(*sorted(anya_set & borya_set))
print(len(anya_set - borya_set))
print(*sorted(anya_set - borya_set))
print(len(borya_set - anya_set))
print(*sorted(borya_set - anya_set))

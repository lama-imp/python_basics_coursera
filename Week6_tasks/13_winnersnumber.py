fin = open('input.txt', 'r', encoding='utf8')
points_9 = []
points_10 = []
points_11 = []

for line in fin:
    temp = list(line.split())
    if temp[2] == '9':
        points_9.append(int(temp[3]))
    elif temp[2] == '10':
        points_10.append(int(temp[3]))
    elif temp[2] == '11':
        points_11.append(int(temp[3]))
points_9.sort()
points_10.sort()
points_11.sort()
print(
    points_9.count(points_9[-1]),
    points_10.count(points_10[-1]),
    points_11.count(points_11[-1])
    )

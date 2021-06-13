n = int(input())
peopleList = []
for i in range(n):
    tempManData = input().split()
    manData = (int(tempManData[0]), tempManData[1])
    peopleList.append(manData)
peopleList.sort()
for manData in peopleList:
    print(' '.join(map(str, manData)))
p = [
    (172, 'Vasya'),
    (180, 'Petya'),
    (172, 'Petya')]
p.sort()
for i in range(len(p)):
    p[i] = (-p[i][0], p[i][1])
print(*p)


def make_tuple(man):
    return (-man[0], man[1])


p.sort(key=make_tuple)
print(*p)
ls = ['abcd', 'bc', '1234']
ls.sort(key=len)
print(*ls)

points = [
    (1, 1),
    (10, 1),
    (5, 5)
]


def sqr_dist(point):
    return point[0] ** 2 + point[1] ** 2


points.sort(key=sqr_dist)
print(*points)

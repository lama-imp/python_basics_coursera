# a = [3, 1, 2]
# a.sort()
# b = sorted(a)  # сортирует все - строки, кортежи, на выходе всегда список
#
# c = sorted(a, reverse=True)
# print(a, b, c)

# print((1, 10) < (2, 'abc'))
p = [
    (172, 'Vasya'),
    (180, 'Petya'),
    (172, 'Petya')]
p.sort(reverse=True)
print(*p)

s = input()
pos = 0
s2 = s[::-1]
a = s.find('h', pos)
c = s2.find('h', pos)
b = len(s) - c
print(s[:a], s[a:b - 1], s[a + 1:b], s[b:], sep='')
# print(s[:a])
# print(s[a:b - 1])
# print(s[a + 1:b])
# print(s[b:])

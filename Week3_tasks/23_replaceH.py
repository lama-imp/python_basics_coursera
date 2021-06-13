s = input()
s2 = s[::-1]
a = s.find('h')
pos2 = a + 1
d = s.find('h', pos2)
c = s2.find('h')
b = len(s) - c - 1
s2 = s[a + 1:b]
if s.count('h') >= 2:
    s2 = s2.replace('h', 'H')

print(s[:a + 1], s2, s[b:], sep='')

s = input()
pos = 0
s2 = s[::-1]
a = s.find('h', pos)
c = s2.find('h', pos)
b = len(s) - c
print(s[:a], s[b:], sep='')

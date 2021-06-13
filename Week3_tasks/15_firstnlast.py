s = input()
pos = 0
s2 = s[::-1]
a = s.find('f', pos)
pos2 = a + 1
d = s.find('f', pos2)
c = s2.find('f', pos)
b = len(s) - c - 1

if a != -1:
    if d != -1:
        print(a, b)
    else:
        print(a)

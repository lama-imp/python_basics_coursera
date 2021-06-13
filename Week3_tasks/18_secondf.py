s = input()
a = s.find('f')
b = s.find('f', a + 1)

if a != -1:
    print(b)
else:
    print(-2)

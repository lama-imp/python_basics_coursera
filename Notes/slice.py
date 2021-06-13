s = 'my name is my'
pos = 0
while s.find('my', pos) != -1:
    print(s.find('my', pos))
    pos = s.find('my', pos) + 1

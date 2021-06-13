def min4(a, b, c, d):
    com1 = min(a, b)
    com2 = min(com1, c)
    com3 = min(com2, d)
    return com3


a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min4(a, b, c, d))

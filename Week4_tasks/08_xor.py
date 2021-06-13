def xor(x, y):
    return x != y


x, y = int(input()), int(input())
if xor(x, y):
    print(1)
else:
    print(0)

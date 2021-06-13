n = int(input())
list = list(map(int, input().split()))
x = int(input())
y = x
z = x

if list.count(x) > 0:
    print(x)
else:
    while list.count(y) == 0 or list.count(z) == 0:
        y -= 1
        z += 1
        if list.count(y) > 0 or list.count(z) > 0:
            break
    if list.count(y) > 0:
        print(y)
    else:
        print(z)

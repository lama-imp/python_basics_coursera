def sum(a, b):
    if a == 0:
        return b
    else:
        a -= 1
        return sum(a, b) + 1


a, b = int(input()), int(input())
print(sum(a, b))

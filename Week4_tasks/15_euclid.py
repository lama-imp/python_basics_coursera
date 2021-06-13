def gcd(a, b):
    if a > b:
        a, b = a, b
    else:
        a, b = b, a
    if a % b != 0:
        return gcd(b, a % b)
    else:
        return b


a, b = int(input()), int(input())
print(gcd(a, b))

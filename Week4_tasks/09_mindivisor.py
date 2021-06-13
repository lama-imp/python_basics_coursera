def min_divisor(n):
    a = 2
    while n % a != 0:
        a += 1
        if a > n ** 0.5:
            return n
    return a


n = int(input())
print(min_divisor(n))

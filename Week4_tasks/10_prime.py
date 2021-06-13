def is_prime(n):
    divisor = 2
    while n % divisor != 0:
        divisor += 1
        if divisor > n ** .5:
            divisor = n
    return divisor == n


n = int(input())

if is_prime(n):
    print('YES')
else:
    print('NO')

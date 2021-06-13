def palindrom(n):
    a = str(n // 1000)
    b = str((n % 1000) // 100)
    c = str((n % 100) // 10)
    d = str(n % 10)
    sum = d + c + b + a
    return int(sum) == n


a, b = int(input()), int(input())
for i in range(a, b + 1):
    if palindrom(i):
        print(i)

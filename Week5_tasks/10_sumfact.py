def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += factorial(i)
print(sum)

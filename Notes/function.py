def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def pasctri(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def max2(a, b):
    if a > b:
        return a
    else:
        return b


def max3(a, b, c):
    return max2(max2(a, b), c)


def sort2(a, b):
    if a < b:
        return a, b
    else:
        return b, a


min, max = sort2(5, 4)
print(min, max)


def is_even(n):
    return n % 2 == 0


n = int(input())
if is_even(n):
    print('even')
else:
    print('odd')

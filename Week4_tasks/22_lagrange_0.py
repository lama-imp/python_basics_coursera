from math import sqrt


def lagrange(n):
    a = int(sqrt(n))
    b = int(sqrt(n - a ** 2))
    c = int(sqrt(a - b ** 2))
    d = int(sqrt(b - c ** 2))
    print(a, b, c, d)
    if a ** 2 + b ** 2 + c ** + d ** 2 == n:
        return a, b, c, d
    else:
        a = int(sqrt(n)) - 1
        b = int(sqrt(n - a ** 2))
        c = int(sqrt(a - b ** 2))
        d = int(sqrt(b - c ** 2))
        print(a, b, c, d)
        if a ** 2 + b ** 2 + c ** + d ** 2 == n:
            return a, b, c, d
        else:
            a = int(sqrt(n)) - 1
            b = int(sqrt(n - a ** 2)) - 1
            c = int(sqrt(a - b ** 2))
            d = int(sqrt(b - c ** 2))
            print(a, b, c, d)
            if a ** 2 + b ** 2 + c ** + d ** 2 == n:
                return a, b, c, d
            else:
                a = int(sqrt(n)) - 1
                b = int(sqrt(n - a ** 2)) - 1
                c = int(sqrt(a - b ** 2)) - 1
                d = int(sqrt(b - c ** 2))
                print(a, b, c, d)
                if a ** 2 + b ** 2 + c ** + d ** 2 == n:
                    return a, b, c, d
                else:
                    a = int(sqrt(n)) - 1
                    b = int(sqrt(n - a ** 2)) - 1
                    c = int(sqrt(a - b ** 2)) - 1
                    d = int(sqrt(b - c ** 2)) - 1
                    print(a, b, c, d)
                    if a ** 2 + b ** 2 + c ** + d ** 2 == n:
                        return a, b, c, d


# n = int(input())
n = 23


print(lagrange(n))

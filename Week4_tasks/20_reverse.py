def reverse():
    n = int(input())
    if n == 0:
        print(0)
    else:
        reverse()
        print(n)


reverse()

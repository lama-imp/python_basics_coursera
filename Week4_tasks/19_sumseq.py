def sumseq():
    n = int(input())
    if n == 0:
        return 0
    else:
        return n + sumseq()


print(sumseq())

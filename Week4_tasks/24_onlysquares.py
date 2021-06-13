def seq_square():
    n = int(input())
    if n != 0:
        if n % (n ** .5) == 0:
            seq_square()
            print(str(n), end=' ')

        else:
            seq_square()


seq_square()

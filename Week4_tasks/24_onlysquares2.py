def seq_square():
    n = int(input())
    if n != 0:
        if n % (n ** .5) == 0:
            return str(seq_square()) + ' ' + str(n)
        else:
            seq_square()
    else:
        return


# if seq_square() is not None:
#     seq_square()
# else:
print(seq_square())

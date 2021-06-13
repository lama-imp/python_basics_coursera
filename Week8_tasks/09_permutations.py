from itertools import permutations

list(map(
    lambda x: print(*x, sep=''),
    permutations(range(1, int(input()) + 1))
))

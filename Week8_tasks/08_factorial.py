from itertools import accumulate
from operator import mul

print(1, *accumulate(
    range(1, int(input()) + 1),
    mul
))

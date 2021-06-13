import itertools
import functools

print(*itertools.combinations([1, 2, 3], 2))
print(*itertools.permutations([1, 2, 3]))
print(*itertools.permutations([1, 2, 3], 2))
print(*itertools.combinations_with_replacement([1, 2, 3], 2))

prints = functools.partial(print, end=' ')
'''
Задание существующей функции параметров по умолчанию
'''

print(functools.reduce(lambda x, y: x + y, [1, 2, 3]))

print(*itertools.accumulate([1, 4, 3, 5], max))

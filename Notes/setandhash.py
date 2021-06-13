set1 = {1, 2, 3}
set2 = {3, 1, 2}
print(set == set2)

my_list = map(int, input().split())
my_set = set(my_list)
print(my_set)

my_set = {1, 3.14, 'abc', (1, 2), frozenset((1, 2))}
print(frozenset(my_set))
print(*my_set)

my_set = {1, 2, 3, 1, 400000000}
print(sorted(list(my_set)))

my_set = set('abcdabc')
print(len(my_set))

primes = {2, 3, 5, 7, 11, 13}
n = int(input())
if n in primes:
    print('in set')
else:
    print('not in set')

if n not in primes:
    print('not in set')
else:
    print('in set')

primes.add(17)
primes.remove(13)  # при отсутсвии элемента - ломается
primes.discard(11)  # при отсутствии элемента не делает ничего
print(*primes)
a = {1, 2, 3, 4}
b = {1, 3, 5}
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a | b)  # объединение множеств
print(a & b)  # пересечение множеств
print(a - b)  # все элементы, которые содержатся во множестве а и не содержатся во множетсве б
print(a ^ b)  # все элементы, входящие в обхединение множеств, но не входящие в их пересечение

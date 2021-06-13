a = [1, (2, 3), 'a', [5, 6]]
# b = a[:]
b = [1, 2, 3]
a[0] = 4
print(a)


def replacefirst(fList):
    fList[0] = 0


a = [1, 2, 3]
replacefirst(a)
print(a)


def reverse(fList):
    a = fList[::-1]
    fList[:] = ''
    fList[:] = a


a = [1, 2, 3]
reverse(a)
print(a)


a = list('abcde')
a[0] = 'f'
s = ''.join(a)
print(s)


word_list = input().split()
print(word_list)

word_list = input().split('a')
print(word_list)


int_list = list(map(int, input().split()))
print(' '.join(map(str, int_list)))
print(*int_list)


a = [1, 2, 3, 4, 5, 6, 2, 2, 3]
print(a.count(8))

b = a.copy()
a.extend(b)
a.remove(2)
a.append(5)
a.insert(0, 10)
a.pop(0)
print(a)


a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i] % 2 != 0:
        a.pop(i)  # does not work!!!
i = 0
while i < len(a):
    if a[i] % 2 != 0:  # works slowly
        a.pop(i)
    else:
        i += 1

b = []
for i in a:
    if i % 2 == 0:  # works fast but more memory
        b.append(i)
print(*b)

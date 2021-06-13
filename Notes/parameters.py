def print_list(lst, mysep):
    for i in range(len(lst) - 1):
        print(lst[i], mysep, sep='', end='')
    print(lst[i], sep='')


def print_list2(lst, mysep=' '):
    for i in range(len(lst)):
        print(lst[i], mysep, sep='', end='')


print_list([1, 2, 3], 'a')
print_list2([1, 2, 3], '_')
print()


def my_sum(*args):  # неопределенное количество параметров
    return sum(args)


print(my_sum(1, 2, 3, 4))

print(sum([1, 2, 3]))


def my_min(first, *others):
    nowmin = first
    for now in others:
        if now < nowmin:
            nowmin = now
    return nowmin


print(my_min(7, 2, 5))

new = input()
first, second, third = input(), input(), input()
phbook = [new, first, second, third]
mod_phbook = []
for number in phbook:
    mod_number = ''
    for i in number:
        if i.isdigit():
            mod_number += i
    if len(mod_number) == 7:
        mod_number = '495' + mod_number
    elif len(mod_number) > 10:
        mod_number = mod_number[1:]
    mod_phbook.append(mod_number)
for number in mod_phbook[1:]:
    if number == mod_phbook[0]:
        print('YES')
    else:
        print('NO')

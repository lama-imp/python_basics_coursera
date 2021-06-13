cow = int(input())
n = cow % 10
if 10 < cow < 20:
    print(cow, 'korov')
elif n == 1:
    print(cow, 'korova')
elif n == 2 or n == 3 or n == 4:
    print(cow, 'korovy')
else:
    print(cow, 'korov')

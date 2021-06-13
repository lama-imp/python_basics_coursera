a = int(input())
b = int(input())

while a != b:
    if a // 2 >= b:
        if a % 2 == 0:
            print(':2')
            a = a // 2
        else:
            print('-1')
            a -= 1
    else:
        print('-1')
        a -= 1

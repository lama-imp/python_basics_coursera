a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
l1 = a1
w1 = b1
h1 = c1
if a2 >= b2 and a2 >= c2:
    (l2, w2, h2) = (a2, b2, c2)
elif b2 >= c2 and b2 >= a2:
    (l2, w2, h2) = (b2, a2, c2)
else:
    (l2, w2, h2) = (c2, a2, b2)
if h2 > w2:
    (w2, h2) = (h2, w2)
# print(l2, w2, h2)
num1 = (l1 // l2) * (w1 // w2) * (h1 // h2)
num2 = (l1 // w2) * (w1 // l2) * (h1 // h2)
num3 = (l1 // h2) * (w1 // w2) * (h1 // l2)
num4 = (l1 // w2) * (w1 // h2) * (h1 // l2)
# print(num1, num2, num3, num4)
if num1 >= num2:
    if num2 >= num3 or num1 > num3:
        if num1 >= num4:
            print(num1)
        else:
            print(num4)
    elif num3 >= num4:
        print(num3)
    else:
        print(num4)
elif num2 >= num3:
    if num2 >= num4:
        print(num2)
    else:
        print(num4)
else:
    if num3 >= num4:
        print(num3)
    else:
        print(num4)

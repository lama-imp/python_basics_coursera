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
num5 = (l1 // l2) * (w1 // h2) * (h1 // w2)
num6 = (l1 // h2) * (w1 // l2) * (h1 // w2)
if num1 >= num2:
    if num2 >= num3 or num1 > num3:
        max1 = num1
    else:
        max1 = num3
elif num2 >= num3:
    max1 = num2
else:
    max1 = num3
if num4 >= num5:
    if num5 >= num6 or num4 > num6:
        max2 = num4
    else:
        max2 = num6
elif num5 >= num6:
    max2 = num5
else:
    max2 = num6
if max1 >= max2:
    print(max1)
else:
    print(max2)

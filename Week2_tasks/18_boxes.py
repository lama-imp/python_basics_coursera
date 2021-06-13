a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if a1 >= b1 and a1 >= c1:
    (l1, w1, h1) = (a1, b1, c1)
elif b1 >= c1 and b1 >= a1:
    (l1, w1, h1) = (b1, a1, c1)
else:
    (l1, w1, h1) = (c1, a1, b1)
if w1 > h1:
    (w1, h1) = (h1, w1)
# print(w1, h1, l1)
if a2 >= b2 and a2 >= c2:
    (l2, w2, h2) = (a2, b2, c2)
elif b2 >= c2 and b2 >= a2:
    (l2, w2, h2) = (b2, a2, c2)
else:
    (l2, w2, h2) = (c2, a2, b2)
if w2 > h2:
    (w2, h2) = (h2, w2)
# print(w2, h2, l2)
if w1 == w2 and h1 == h2 and l1 == l2:
    print('Boxes are equal')
elif w1 >= w2 and h1 >= h2 and l1 >= l2:
    print('The first box is larger than the second one')
elif w1 <= w2 and h1 <= h2 and l1 <= l2:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')

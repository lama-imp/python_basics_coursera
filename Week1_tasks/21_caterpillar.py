h = int(input())
a = int(input())
b = int(input())
# h = 2
# a = 3
# b = 0
# print((h + (a - b + a - 1)) // ((a - b) + a))
# print(h // a + h // b)
# c = 0 ** b
# no_b = c*((h + a - 1) // a)
# com = (h - b) // (a - b)
# big_b = 0 ** com
# print(no_b + com + big_b)
# print(no_b, com, big_b)
print((h-a + (a - b - 1)) // (a - b) + 1)

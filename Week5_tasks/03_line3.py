n = int(input())
x = 0
while x != n:
    x += 1

start = 10 ** x - 1
if n == 1:
    end = 0
else:
    end = 10 ** (x - 1)
for i in range(start, end, -2):
    print(i, end=' ')

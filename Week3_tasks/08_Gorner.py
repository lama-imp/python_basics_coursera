n = int(input())
x = float(input())
a1 = float(input())
count = 0

while count < n:
    count += 1
    a2 = float(input())
    form = a1 * x + a2
    a1 = form

if n == 0:
    form = a1
print(form)

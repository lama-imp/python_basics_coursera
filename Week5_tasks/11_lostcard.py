n = int(input())
sum = 0
count = 1
while count < n:
    m = int(input())
    count += 1
    sum += m
control = 0
for i in range(1, n + 1):
    control += i
print(control - sum)

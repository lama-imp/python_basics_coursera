now = int(input())
n = 0
sum_seq = now
while now != 0:
    now = int(input())
    sum_seq += now
    n += 1
print(sum_seq / n)

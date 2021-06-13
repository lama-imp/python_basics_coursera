n = float(input())
a = n - int(n)
b = round(a, 1)
if b >= 0.5:
    answer = int(n) + 1
elif b < 0.5:
    answer = int(n)
print(answer)

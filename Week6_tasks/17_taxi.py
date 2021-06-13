fin = open('input.txt', 'r', encoding='utf8')
kmeters = list(map(int, fin.readline().split()))
rates = list(map(int, fin.readline().split()))
kmeters.sort()
rates.sort(key=lambda x: -x)
sum = 0
for i in range(len(kmeters)):
    sum += kmeters[i] * rates[i]
print(sum)

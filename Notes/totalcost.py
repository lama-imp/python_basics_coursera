a = int(input())
b = int(input())
c = int(input())
d = int(input())
cost1 = a * 100 + b
cost2 = c * 100 + d
totcost = cost1 + cost2
print(totcost // 100, totcost % 100, sep='.')

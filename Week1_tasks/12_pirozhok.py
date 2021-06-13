a = int(input())
b = int(input())
n = int(input())
cost = a*100 + b
totcost = cost * n
print(totcost // 100, totcost % 100)

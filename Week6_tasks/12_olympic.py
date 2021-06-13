n = int(input())
lst = []
for i in range(n):
    temp = list(input().split())
    temp2 = int(temp[1]), temp[0]
    lst.append(temp2)
lst.sort(key=lambda x: -x[0])
for item in lst:
    print(item[1])

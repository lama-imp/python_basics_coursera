list = list(map(int, input().split()))
ans = 10000000000000
for i in list:
    if i % 2 != 0 and i < ans:
        ans = i
print(ans)

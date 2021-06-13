list = list(map(int, input().split()))
list.insert(0, list.pop())
print(*list)

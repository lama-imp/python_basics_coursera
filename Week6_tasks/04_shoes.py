size = int(input())
shoes = list(map(int, input().split()))
shoes.sort()
count = 0
now = 0
for i in shoes:
    if count == 0 and i >= size:
        count += 1
        now = i
    elif count != 0 and i >= now + 3:
        count += 1
        now = i
print(count)

temp = list(map(int, input().split()))
size = temp[0]
number = temp[1]
users = []
count = 0
while count < number:
    users.append(int(input()))
    count += 1
users.sort()
reducer = -1
users_size = 0
for i in users:
    users_size += i

while users_size > size:
    users_size -= users[reducer]
    reducer -= 1
    number -= 1

print(number)

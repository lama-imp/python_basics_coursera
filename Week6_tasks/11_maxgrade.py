fin = open('input.txt', 'r', encoding='utf8')
answer = [0, 0, 0]
for line in fin:
    temp = list(line.split())
    if temp[2] == '9':
        if answer[0] < int(temp[3]):
            answer[0] = int(temp[3])
    elif temp[2] == '10':
        if answer[1] < int(temp[3]):
            answer[1] = int(temp[3])
    elif temp[2] == '11':
        if answer[2] < int(temp[3]):
            answer[2] = int(temp[3])
print(*answer)

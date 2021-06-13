fin = open('input.txt', 'r', encoding='utf8')
answer = []
for line in fin:
    lst = list(line.split())
    temp = (lst[0], lst[1], lst[3])
    answer.append(temp)
answer.sort()
for i in range(len(answer)):
    print(*answer[i])

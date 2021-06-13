fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

n = int(fin.readline())
persons = []
for line in fin:
    temp = list(line.split())
    temp2 = list(map(int, temp[-1:-4:-1]))
    count = 0
    for i in temp2:
        if i < 40:
            count += 1
    if count == 0:
        persons.append(temp2)
grades = []
if len(persons) <= n:
    print(0, file=fout)
elif len(persons) != 0:
    for person in persons:
        grades.append(sum(person))
    grades.sort(key=lambda x: -x)
    grades_number = []
    prev_num = 0
    for num in range(len(grades)):
        num = grades[num]
        if num != prev_num:
            grades_number.append(grades.count(num))
        prev_num = num
    accepted = 0
    for grade in grades_number:
        if accepted + grade < n:
            accepted += grade
        elif accepted + grade == n:
            accepted += grade
            break
        else:
            break
    if accepted == 0:
        print(1, file=fout)
    else:
        print(grades[accepted - 1], file=fout)
    fout.close()

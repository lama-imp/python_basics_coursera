def average(lst):
    return sum(lst) / len(lst)


fin = open('input.txt', 'r', encoding='utf8')
nine = []
ten = []
eleven = []
for line in fin:
    lst = list(line.split())
    # print(lst)
    if lst[2] == '9':
        nine.append(int(lst[3]))
    elif lst[2] == '10':
        ten.append(int(lst[3]))
    elif lst[2] == '11':
        eleven.append(int(lst[3]))

# print(nine, ten, eleven)
print(average(nine), average(ten), average(eleven))

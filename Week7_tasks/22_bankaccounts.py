def deposit(name, sum):
    clients[name] = clients.get(name, 0) + sum


def withdraw(name, sum):
    clients[name] = clients.get(name, 0) - sum


def balance(name):
    if name in clients:
        print(clients[name])
    else:
        print('ERROR')


def transfer(name1, name2, sum):
    clients[name1] = clients.get(name1, 0) - sum
    clients[name2] = clients.get(name2, 0) + sum


def income(procent):
    for client in clients:
        if clients[client] > 0:
            income = int(clients[client] * procent / 100)
            clients[client] += income


clients = dict()
file = open('input.txt')
for line in file:
    temp = line.split()
    if temp[0] == 'DEPOSIT':
        deposit(temp[1], int(temp[2]))
    elif temp[0] == 'WITHDRAW':
        withdraw(temp[1], int(temp[2]))
    elif temp[0] == 'BALANCE':
        balance(temp[1])
    elif temp[0] == 'TRANSFER':
        transfer(name1=temp[1], name2=temp[2], sum=int(temp[3]))
    elif temp[0] == 'INCOME':
        income(int(temp[1]))

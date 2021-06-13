file = open('input.txt')
buyers = dict()
for line in file:
    temp = line.split()
    buyer = temp[0]
    item = temp[1]
    number = int(temp[2])
    bought = {item: number}
    buyers[buyer] = buyers.get(buyer, {})
    buyers[buyer][item] = buyers[buyer].get(item, 0) + number
for buyer in sorted(buyers):
    print(buyer, ':', sep='')
    for item in sorted(buyers[buyer]):
        print(item, buyers[buyer][item])

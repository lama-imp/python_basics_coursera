fin = open('input.txt', 'r', encoding='utf8')
word_count = set()
for line in fin:
    temp = line.split()
    for i in temp:
        word_count.add(i)
print(len(word_count))

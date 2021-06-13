fin = open('test.txt', 'r', encoding='utf8')

a = int(fin.readline())
b = int(fin.readline())
print(a + b)

lines = fin.readlines()
print(lines[0].strip(), lines[1].strip())

for line in fin:
    print(int(line) + 1)

s = fin.read()  # чтение всего файла до конца в одну строку
print([s])

fout = open('output.txt', 'w', encoding='utf8')
print(sum(map(int, fin.readlines())), file=fout)
fout.close()

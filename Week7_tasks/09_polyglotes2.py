fin = open('input.txt', 'r', encoding='utf8')

n = int(fin.readline())

all_know = set()
others = set()
boy = set()
count = 0

for lang in fin:
    lang = lang.strip()
    if lang.isdigit():
        for item in range(int(lang)):
            curlang = fin.readline().strip()
            boy.add(curlang)
            others.add(curlang)
        if count == 0:
            all_know = all_know | boy
        else:
            all_know = all_know & boy
        boy = set()
        count += 1


print(len(all_know), *all_know, len(others), *others, sep='\n')

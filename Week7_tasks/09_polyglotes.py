fin = open('input.txt', 'r', encoding='utf8')

n = int(fin.readline())
# poly_list = [set()] * n
boy = 0

all_know = set()
others = set()
boy = set()

for lang in fin:
    lang = lang.strip()
    if lang.isdigit():
        # if len(boy) == 0 and len(allknow) == 0:
        #     continue
        # else:
        print(boy)
        if len(all_know) == 0 and len(boy) != 0:
            print('1 if')
            all_know |= boy
        elif len(all_know) != 0:
            print('2 if')
            all_know &= boy
        boy = set()
    else:
        boy.add(lang)
        others.add(lang)
# print('list', poly_list)

# for person in poly_list:
#     if len(all_know) == 0:
#         all_know.add(person)
#     else:
#         all_know &= person
#     others.add(person)
print(len(all_know), all_know, len(others), others, sep='\n')

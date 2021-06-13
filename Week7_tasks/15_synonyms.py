file = open('input.txt')
n = int(file.readline().strip())
synonyms = dict()
for num in range(n):
    pair = file.readline().split()
    synonyms[pair[0]] = pair[1]
search_item = file.readline().strip()
try:
    print(synonyms[search_item])
except KeyError:
    for word in synonyms:
        if search_item in synonyms[word]:
            print(word)
            break

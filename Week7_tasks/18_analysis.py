def sort_key(item):
    return -item[0], item[1]


file = open('input.txt')
words = dict()
for line in file:
    for word in line.split():
        words[word] = words.get(word, 0) + 1
answer = []
for word in words:
    # item = (words[word], word)
    answer.append((words[word], word))
answer.sort(key=sort_key)
for item in answer:
    print(item[1])

file = open('input.txt')
words = []
for line in file:
    words.extend(list(line.split()))
words_count = dict()
for word in words:
    words_count[word] = words_count.get(word, 0)
    print(words_count[word], end=' ')
    words_count[word] += 1

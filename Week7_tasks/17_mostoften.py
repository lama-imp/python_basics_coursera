file = open('input.txt')
text = []
for line in file:
    text.extend(line.strip().split())
words = dict()
for word in text:
    words[word] = words.get(word, 0) + 1
counter = 0
answer = ''
for word in sorted(words):
    if words[word] > counter:
        counter = words[word]
        answer = word
print(answer)

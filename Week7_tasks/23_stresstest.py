file = open('input.txt')
n = int(file.readline())
dictionary = dict()
for i in range(n):
    line = file.readline().strip()
    word = line.lower()
    if word in dictionary:
        dictionary[word].append(line)
    else:
        dictionary[word] = [line, ]

text = file.readline().split()
errors_count = 0
for word in text:
    if word.lower() in dictionary:
        if word not in dictionary[word.lower()]:
            errors_count += 1
    else:
        count_up = 0
        for char in word:
            if char.isupper():
                count_up += 1
        if count_up != 1:
            errors_count += 1

print(errors_count)

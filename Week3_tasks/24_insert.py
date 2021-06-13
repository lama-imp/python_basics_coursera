s = input()
a = 0
count = 0
b = ''
while count < len(s):
    count += 1
    b += s[a:a + 1] + '*'
    a += 1
print(b[:-1])

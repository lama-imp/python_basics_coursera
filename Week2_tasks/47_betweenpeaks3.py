n = int(input())
prev = 0
prev_prev = 0
b = 0  # счетчик количества максимумов
count_n = 0  # координата текущей точки
count_1 = 0  # коррдината максимума 1
count_2 = 0  # коррдината максимума 2
count_dif = 0
count = 0  # минимальное расстояние между максимумами

while n != 0:
    count_n += 1
    if prev > prev_prev and prev > n:
        b += 1
        count_1 = count_2
        count_2 = count_n - 1
        count_dif = count_2 - count_1
        if b >= 2:
            if count == 0 or count > count_dif:
                count = count_dif
            else:
                count = count
    # print(b, count_n, count_1, count)
    prev_prev = prev
    prev = n
    n = int(input())

if b <= 1:
    print(0)
else:
    print(count)

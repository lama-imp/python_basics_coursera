height_list = list(map(int, input().split()))
pet_height = int(input())

for i, h in enumerate(height_list):
    if h < pet_height:
        print(i + 1)
        break
if pet_height <= height_list[-1]:
    print(len(height_list) + 1)

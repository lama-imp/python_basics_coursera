file = open('input.txt')
countries_dict = dict()
countries_number = int(file.readline().strip())
for line in range(countries_number):
    temp_list = list(file.readline().split())
    countries_dict[temp_list[0]] = set(temp_list[1:])
cities_number = int(file.readline().strip())
for i in range(cities_number):
    city = file.readline().strip()
    for country in countries_dict:
        if city in countries_dict[country]:
            print(country)
            break

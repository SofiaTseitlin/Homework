import sys
try:
    text_file = open("cities.txt", 'r')
except FileNotFoundError:
    print("Файл cities.txt не найден")
    sys.exit()
cities = {}
for line in text_file:
    row = line.rstrip().split(":")
    cities[row[0]] = row[1]
cities = dict(sorted(cities.items()))
minimum = int(input("Введите минимальное количество жителей: "))
with open("filtered_cities.txt", 'w') as text_file_2:
    for city in cities:
        if int(cities[city]) > minimum:
            text_file_2.write(city + ":" + cities[city] + '\n')
text_file.close()
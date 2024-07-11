import sys

try:
    text_file = open("input.txt", 'r')
except FileNotFoundError:
    print("Файл input.txt не найден")
    sys.exit()
information = {}
for line in text_file:
    row = line.rstrip().split(":")
    information[row[0]] = row[1]
lesson = input("Введите название курса: ")
for row in information:
    if lesson in information[row]:
        print(row)
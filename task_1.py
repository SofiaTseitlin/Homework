import sys
try:
    text_file = open("input.txt", "r")
except FileNotFoundError:
    print("Файл input.txt не найден")
    sys.exit()
summa = 0
quantity = 0
information = []
for line in text_file:
    information.append(line.split())
for row in information:
    for element in row:
        if element.isdigit():
            summa += int(element)
            quantity += 1
average = summa / quantity
with open("output.txt", "w") as output:
    for row in information:
        if int(row[1]) > average:
            output.write(row[0] + row[1] + '\n')
text_file.close()
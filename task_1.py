text_file = open("input.txt", "r")
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
        if int(row[1]) >= average:
            output.write(str(row) + '\n')
output.close()
text_file.close()

import sys
try:
    text_file_1 = open('input1.txt', 'r')
except FileNotFoundError:
    print("Файл input1.txt не найден.")
    sys.exit()
try:
    text_file_2 = open('input2.txt', 'r')
except FileNotFoundError:
    print("Файл input2.txt не найден.")
    sys.exit()
text_file_3 = open('output.txt', 'w')
rows = []
for line in text_file_1:
    rows.append(line.rstrip())
for line in text_file_2:
    rows.append(line.rstrip())
rows = sorted(rows)
for row in rows:
    text_file_3.write(row + '\n')
text_file_1.close()
text_file_2.close()
text_file_3.close()
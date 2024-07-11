text_file_1 = open('input1.txt', 'r')
text_file_2 = open('input2.txt', 'r')
text_file_3 = open('output.txt', 'w')
rows = []
for line in text_file_1:
    rows.append(line.split())
for line in text_file_2:
    rows.append(line.split())
rows = sorted(rows)
print(rows, file=text_file_3)
text_file_1.close()
text_file_2.close()
number = input()
while not number.isdigit():
    number = input("Введите число: ")
summa = int(number)
while summa > 9:
    summa = 0
    for i in number:
        summa += int(i)
    number = str(summa)
print(summa
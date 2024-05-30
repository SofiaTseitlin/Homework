number = input("Введите число от 1 до 999: ")
while not number.isdigit() or not(1 <= int(number) <= 999):
    number = input("Введите число от 1 до 999: ")
number = int(number)
e = number % 10
e_d = number % 100
d = number % 100 // 10
s = number // 100
spisok_e = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
spisok_e_d = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
spisok_d = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят","девяносто"]
spisok_s = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
answer = ""
if s != 0:
    answer += spisok_s.pop(s - 1)
    answer += " "
if 11 <= e_d <= 19:
    answer += spisok_e_d.pop(number // 100)
    answer += " "
else:
    if d != 0:
        answer += spisok_d.pop(d - 1)
        answer += " "
    if e != 0:
        answer += spisok_e.pop(e - 1)
        answer += " "
print(answer)
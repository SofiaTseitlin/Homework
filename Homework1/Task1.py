n = input("Введите желаемое количество строк для тругольника: ")
while not n.isdigit():
    n = input("Введите, пожалуйста, число: ")
n = int(n)
for i in range(n):
    space = n - i - 1
    stars = 2 * i + 1
    print(" " * space + "*" * stars)
x = 2
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
a1 = a
b1 = b

while a1 != 0 and b1 !=0:
    if a1 > b1:
        a1 = a1 % b1
    else:
        b1 = b1 % a1
c = a1 + b1
print("Наибольший общий делитель:", c)
d = (a * b) / c
print("Наименьшее общее кратное", d)



def kopim_denezhki(vklad, percent, a):
    while a > 0:
        clear_percent = vklad * percent

        vklad = vklad + clear_percent

        a = a - 1
            
    return vklad



while True:
    try:
        a = int(input('Введите срок вклада: '))
    except:
        print('Вы ввели неверное значение. Введите числовое значение!')
        continue
    try:
        vklad = int(input('Введите сумму вклада: '))
    except:
        print('Вы ввели неверное значение. Введите числовое значение!')
        continue
    try:
        percent = int(input('Введите процент по вкладу: '))
    except:
        print('Вы ввели неверное значение. Введите числовое значение!')
        continue
    break

n = vklad
m = percent
percent = percent / 100

k = kopim_denezhki(vklad, percent, a)


z = k - n
print("Чистая прибыль по вложенной сумме в размере ", n, ' рублей по процентной ставке ', m, '%, на срок ', a, ' месяц(ев), составит', z, 'рублей.\n Текущая сумма на счете ', k, ' рублей.')

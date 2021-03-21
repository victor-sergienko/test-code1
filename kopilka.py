
# Функция подсчета выгоды по вкладу

def kopim_denezhki(vklad, percent, a):
    while a > 0:
        clear_percent = vklad * percent
        vklad = vklad + clear_percent
        a = a - 1
    return vklad

# Выбор действия с программой
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



percent = percent / 100

k = kopim_denezhki(vklad, percent, a)

# Высчитываем итоговую чистую прибыль
z = k - vklad
print("Чистая прибыль по вложенной сумме в размере ", n, ' рублей по процентной ставке ', percent, '%, на срок ', a, ' месяц(ев), составит', z, 'рублей.\n Текущая сумма на счете ', k, ' рублей.')

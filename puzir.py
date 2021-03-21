# Импортируем модуль рандом
import random


while True:
    
    # Выбор метода обработки
    try:
        start = int(input('введите, что вы хотите обрабатывать 1 - строку, 2 - массив, 3 - выход: '))
    except:
        print('Вы ввели неверное значение. Введите числовое значение: ')
        continue
    
    
    # Сортируем массив
    if start == 2:
        while True:
            # Получение и проверка значений
            try:
                a1 = int(input("введите начальное значение диапазона: "))
                b1 = int(input("введите конечное значение диапазона: "))
            except:
                print('Вы ввели неверное значение. Введите числовое значение: ')
                continue
            # Выполняем сортировку пузырьковым методом
            k = 10
            arr = []
            print(a1,b1)
            if a1 > b1:
                a1,b1 = b1,a1
            print(a1,b1)
            for i in range(k):
                arr.append(random.randint(a1,b1))
            print(arr)
            for i in range(k-1):
                for j in range(k-i-1):
                    if arr[j] > arr[j+1]:
                        arr[j], arr[j+1] = arr[j+1], arr[j]
            # Выводим результат сортировки
            print(arr)
            break
                       
    
    # Сортируем строки
    elif start == 1:
        # Дополнительно импортируем модули для сортировки
        from random import choice
        from string import ascii_uppercase
        # Выполняем сортировку при помощи модулей
        c = (''.join(choice(ascii_uppercase) for i in range(12)))
        g = ''.join(sorted(c))
        print('Сгенерированная строка: ', c)
        print("Отсортированная строка: ", g)

    # Выход из программы
    elif start == 3:
        exit('Goodbye!')


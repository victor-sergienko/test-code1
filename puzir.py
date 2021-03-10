import random

while True:
    

    try:
               start = int(input('введите, что вы хотите обрабатывать 1 - строку, 2 - массив, 3 - выход: '))
    except:
        print('Вы ввели неверное значение. Введите числовое значение: ')
        continue





    if start == 2:
        while True:
            try:
                a1 = int(input("введите начальное значение диапазона: "))
                b1 = int(input("введите конечное значение диапазона: "))
            except:
                print('Вы ввели неверное значение. Введите числовое значение: ')
                continue
            
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
            print(arr)
            break
            
            
    

    elif start == 1:
        from random import choice
        from string import ascii_uppercase

        c = (''.join(choice(ascii_uppercase) for i in range(12)))
        g = ''.join(sorted(c))
        print('generated string: ', c)
        print("sorted string: ", g)


    elif start == 3:
        exit('Goodbye!')


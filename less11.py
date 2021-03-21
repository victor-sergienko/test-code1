# Задаем цикл пересчета от 1 до 100
for i in range(0,100):
    #Проверяем кратность 15
    if i % 3 == 0 and i % 5 == 0:
        print(' FizzBuzz ')
    # Проверяем кратность 3, но не 5
    elif i % 3 == 0 and i % 5 != 0:
        print(' Fizz ')
    # Проверяем кратность 5, но не 3
    elif i % 3 != 0 and i % 5 == 0:
        print(' Buzz ')
    else: 
        print(i)

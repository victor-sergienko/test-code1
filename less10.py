
# Импортируем функции счетчика, рандома и времени
from collections import Counter
import random
import time

#Задаем время генерации чисел на 3 секунды
t_end = time.time() + 3

# Объявляем массив, в который сложим числа
arr = []

# Подбираем рандомно числа, в рамках границ времени
while time.time() < t_end:
    #print(time.time())
    arr.append(random.randint(0,100))

# Получаем 5 самых часто-встречаемых чисел
arr = Counter(arr)
print(arr.most_common(5))



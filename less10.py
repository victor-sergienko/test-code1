from collections import Counter
import random
import time
#Задаем время генерации чисел в 3 секунды
t_end = time.time() + 3
arr = []

while time.time() < t_end:
    #print(time.time())
    arr.append(random.randint(0,100))

# Получаем 5 самых часто-встречаемых чисел
arr = Counter(arr)
print(arr.most_common(5))



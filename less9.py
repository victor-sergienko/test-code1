
# Получаем строку и выполняем подсчет всех символов в ней
string = input("Введите предложение: ")
f = {}
for i in string:
    f[i]=f.get(i,0)+1
print(f)


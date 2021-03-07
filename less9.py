


# Считаем вообще все символы
string = input("Введите предложение: ")
f = {}
for i in string:
    f[i]=f.get(i,0)+1
print(f)


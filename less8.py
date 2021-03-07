
# Функция шифрования
def xor_cipher(str, key):
    encript_str = ""
    for letter in str:
        encript_str += chr( ord(letter) ^ key )
    return encript_str
#
print("Варианты ввода: 1 - зашифровать, 2 - расшифровать сообщение, 3 - выход ")
while True:
    # Проверяем наличие ошибок во введенном значении (значение должно быть числовым и не ломать программу, иначе просим ввести повторно)
    try:
        a = int(input("Что вы хотите сделать? ")) 
    except:
        print('Вы ввели неверное значение. Введите любое из предложенных значений: \n 1 - зашифровать, 2 - расшифровать сообщение, 3 - выход ')
        continue
    # При успешном прохождении проверки, выполняем функцию в соответсвтии с выбором
    if a == 1: 
        strg = str(input("Введите строку, которую хотите зашифровать: "))
        key = int(input("Введите ключ: "))
        print( "Введенное значение:\t", strg)
        encr_strg = xor_cipher( strg, key )
        print( "Зашифрованное значение:\t", encr_strg )
        # print( "Дешифрованное значение:\t", xor_cipher( encr_strg,key )) 

    elif a == 2: 
        strg = str(input("Введите строку, которую хотите дешифровать: "))
        key = int(input("Введите ключ: "))
        print( "Введенное значение:\t", strg)
        print( "Дешифрованное значение:\t", xor_cipher( strg,key ))    

    elif a == 3:
        exit("Всего хорошего!")
    # При несоответствии числа введенным вариантам, отправляем на повторный выбор операции
    else:
        print('Вы ввели неверное значение. Введите любое из предложенных значений: \n 1 - зашифровать, 2 - расшифровать сообщение, 3 - выход ')
        continue



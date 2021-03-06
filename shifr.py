# Функция шифрования
def xor_cipher(str, key):
    encript_str = ""
    for letter in str:
        encript_str += chr( ord(letter) ^ key )
    return encript_str

# Варианты работы с программой 
print("Варианты ввода: 1 - зашифровать, 2 - расшифровать сообщение, 3 - выход ")
while True:
    
    # Проверяем наличие ошибок во введенном значении (значение должно быть числовым и не ломать программу, иначе просим ввести)
    try:
        a = int(input("Что вы хотите сделать? ")) 
    except:
        print('Вы ввели неверное значение. Введите любое из предложенных значений: \n 1 - зашифровать, 2 - расшифровать сообщение, 3 - выход ')
        continue
        
    # При успешном прохождении проверки, выполняем функцию в соответсвтии с выбором
    # Шифрование введенных данных
    if a == 1: 
        input_key = input('Введите ключ шифрования: ')
        input_key = input_key.lower()
        output = []
        for character in input_key:
            number = ord(character) - 96
            output.append(number)
        print(output)
        key = int("".join(str(x) for x in output))
        if key > 500000:
            key = key - 500000 
        with open('test.txt','r') as d:
            strg = d.read()
        print( "Введенное значение:\t", strg)
        encr_strg = xor_cipher( strg, key )
        print( "Зашифрованное значение:\t", encr_strg )
        
        # Запись результата в файл
        with open('test1.txt','w') as d:
            key = d.write(encr_strg)


    # Дешифровка данных
    elif a == 2: 
        input_key = input('Введите ключ шифрования: ')
        input_key = input_key.lower()
        output = []
        for character in input_key:
            number = ord(character) - 96
            output.append(number)
        print(output)
        key = int("".join(str(x) for x in output))
        print('итоговый ключ', key)
        
        # Запись результата в файл
        with open('test1.txt','r') as d:
            strg = d.read()
        
        print( "Введенное значение:\t", strg)
        encr_strg = xor_cipher( strg, key )
        print( "Десшифрованное значение:\t", encr_strg )
        
        with open('test1.txt','w') as d:
            s = d.write(encr_strg)   
    
    # Выход из программы
    elif a == 3:
        exit("Всего хорошего!")
    # При несоответствии числа введенным вариантам, отправляем на повторный выбор операции
    else:
        print('Вы ввели неверное значение. Введите любое из предложенных значений: \n 1 - зашифровать, 2 - расшифровать сообщение, 3 - выход ')
        continue

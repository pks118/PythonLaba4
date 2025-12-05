def text_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

def text_decipher(text, shift):
    return text_cipher(text, -shift)
print("Для выхода введите '0' ")
while True:
    str_input = input("Введите строку: ")
    if str_input == "0":
        print("Выход из программы.")
        break
    try:
        shift = int(input("Введите сдвиг: "))
    except:
        print("Ошибка: необходимо ввести число!")
        continue
    if shift == 0:
        print("Выход из программы.")
        break
    flag = len(str_input) > 0
    if flag:
        encrypted = text_cipher(str_input, shift)
        decrypted = text_decipher(encrypted, shift)
        print(f"Исходный текст: {str_input}")
        print(f"Зашифрованный:  {encrypted}")
        print(f"Расшифрованный: {decrypted}")
    else:
        print("Был замечен неверный паттерн ввода! Убедительная просьба ввести данные повторно!")
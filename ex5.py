print("Для выхода введите '0' ")
while True:
    print("Введите строку: ")
    str_input = input()
    if str_input == "0":
        print("Выход из программы.")
        break
    flag = len(str_input) > 0
    if flag:
        words = str_input.split()
        for word in words:
            print(word)
    else:
        print("Был замечен неверный паттерн ввода! Убедительная просьба ввести данные повторно!")
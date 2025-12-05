print("Для выхода введите '0' ")
while True:
    str_input = input("Введите строку: ")
    if str_input == "0":
        print("Выход из программы.")
        break
    flag = len(str_input) > 0
    if flag:
        words = str_input.split()
        result = " ".join(words)
        print(result)
    else:
        print("Был замечен неверный паттерн ввода! Убедительная просьба ввести данные повторно!")

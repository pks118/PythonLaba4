print("Для выхода введите '0' ")
while True:
    hex_number = input("Введите шестнадцатеричное число: ").strip()
    if hex_number == "0":
        print("Выход из программы.")
        break
    flag = len(hex_number) > 0
    if flag:
        try:
            decimal_number = int(hex_number, 16)
            print(f"Шестнадцатеричное: {hex_number}")
            print(f"Десятичное: {decimal_number}")
        except ValueError:
             print("Ошибка: введено некорректное шестнадцатеричное число")
    else:
        print("Был замечен неверный паттерн ввода! Убедительная просьба ввести данные повторно!")
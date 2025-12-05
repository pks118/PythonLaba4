print("Для выхода введите '0' ")
while True:
    date_str = input("Введите дату в формате ДД.ММ.ГГГГ: ")
    if date_str == "0":
        print("Выход из программы.")
        break
    flag = len(date_str) > 0
    if flag:
        parts = date_str.split('.')
        if len(parts) == 3:
            day, month, year = parts
            print(f"День: {day}")
            print(f"Месяц: {month}")
            print(f"Год: {year}")
        else:
            print("Неверный формат даты!")
    else:
        print("Был замечен неверный паттерн ввода! Убедительная просьба ввести данные повторно!")
def count_glas_soglas_basic(text):
    glas = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    soglas = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    glas_count = 0
    soglas_count = 0
    for char in text:
        if char in glas:
            glas_count += 1
        elif char in soglas:
            soglas_count += 1
    return glas_count, soglas_count

print("Для выхода введите '0' ")
while True:
    str_input = input("Введите строку: ")
    if str_input == "0":
        print("Выход из программы.")
        break
    flag = len(str_input) > 0
    if flag:
        glas = count_glas_soglas_basic(str_input)
        print(f"Гласных, согласных: {glas}")
    else:
        print("Был замечен неверный паттерн ввода! Убедительная просьба ввести данные повторно!")

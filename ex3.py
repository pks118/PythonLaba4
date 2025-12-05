def text_center():
    print("Для выхода введите '0' ")
    while True:
        str_input = input("Введите строку: ")
        if str_input == "0":
            print("Выход из программы.")
            break
        try:
            length_size = int(input("Введите ширину строки: "))
        except ValueError:
            print("Ошибка: необходимо ввести число!")
            continue
        if length_size == 0:
            print("Выход из программы.")
            break
        flag = len(str_input) > 0 and length_size > 0
        count_sym = 0
        for ch in str_input:
            if ch != ' ':
                count_sym += 1
                break
        if flag and count_sym > 0 and (length_size - len(str_input) > 0):
            result = str_input.center(length_size)
            print(f"Исходная строчка: [{str_input}]")
            print(f"Длина исходной строчки: {len(str_input)}\n")
            print(f"Итоговая строчка: [{result}]")
            print(f"Длина итоговой строчки: {len(result)}")
            print(f"Необходимая длина: {length_size}")
        else:
            print("Был замечен неверный паттерн ввода! Убедительная просьба ввести данные повторно!")
        count_sym = 0

def main():
    text_center()

if __name__ == "__main__":
    main()
while True:
    str_input = input("Введите строку (для выхода введите 'y'): ")
    if str_input == 'y':
        print("Выход из программы.")
        break
    flag = len(str_input) != 0
    if not flag:
        print("Строчка пуста!")
        continue
    if flag and (str_input[0] != ' ' and str_input[-1] != ' '):
        result = str_input
    else:
        result = str_input.strip()
    print(f"Исходный вариант: [{str_input}]")
    print(f"Результат: [{result}]")
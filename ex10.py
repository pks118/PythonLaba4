
print("Для выхода введите '0' ")
while True:
    str_input = input("Введите строку: ").strip()
    if str_input == "0":
        print("Выход из программы.")
        break
    if not str_input:
        print("Вы ввели пустую строку!")
    else:
        char_count = len(str_input)
        words = str_input.split()
        word_count = len(words)
        if word_count > 0:
            shortest_word = min(words, key=len)
            longest_word = max(words, key=len)
            print(f"Количество символов: {char_count}")
            print(f"Количество слов: {word_count}")
            print(f"Самое короткое слово: '{shortest_word}' (длина: {len(shortest_word)})")
            print(f"Самое длинное слово: '{longest_word}' (длина: {len(longest_word)})")
        else:
            print("В предложении нет слов!")


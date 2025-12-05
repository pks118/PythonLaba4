def from_latin_to_kirill(symbol, symbols_lat, symbol_kyr):
    """Транслитерация латиницы в кириллицу"""
    for i in range(len(symbols_lat)):
        if symbol == symbols_lat[i]:
            return symbol_kyr[i]
    return symbol

def from_kirill_to_latin(symbol, symbols_kir, symbol_lat):
    """Транслитерация кириллицы в латиницу"""
    for i in range(len(symbols_kir)):
        if symbol == symbols_kir[i]:
            return symbol_lat[i]
    return symbol

symbols_lat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
symbol_kyr = ["а", "б", "к", "д", "е", "ф", "г", "х", "и", "дж", "к", "л", "м", "н", "о", "п", "ку", "р", "с", "т", "у",
              "в", "в", "кс", "йе", "з",
              "А", "Б", "К", "Д", "Е", "Ф", "Г", "Х", "И", "Дж", "К", "Л", "М", "Н", "О", "П", "Ку", "Р", "С", "Т", "У",
              "В", "В", "Кс", "Йе", "З"]
symbols_kir = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
               'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'э', 'ю', 'я',
               'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
               'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы', 'Э', 'Ю', 'Я']
symbol_lat = ["a", "b", "v", "g", "d", "e", "jo", "j", "z", "i", "jo", "k", "l", "m", "n", "o", "p", "r", "s", "т", "u",
              "f", "h", "c", "ch", "sh", "sh'", "i", "a", "ju", "ya",
              "A", "B", "V", "G", "D", "E", "Jo", "J", "Z", "I", "Jo", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U",
              "F", "H", "C", "Ch", "Sh", "Sh'", "I", "A", "Ju", "Ya"]

print("Для выхода введите '0' ")
while True:
    str_input = input("Введите строку: ")
    if str_input == "0":
        print("Выход из программы.")
        break
    flag = len(str_input) > 0
    if flag:
        result = None;
        for i in range(len(str_input)):
            if ord(str_input[i])>=65 and ord(str_input[i]) <= 122:
                result += from_latin_to_kirill(str_input[i], symbols_lat, symbol_kyr)
            else:
                result += from_kirill_to_latin(str_input[i], symbols_kir, symbol_lat)
        print(result)
    else:
        print("Был замечен неверный паттерн ввода! Убедительная просьба ввести данные повторно!")
import ex11
import ex3
import ex2
def main():
    flag = True
    while flag:
        print("Выберите пункт меню:")
        print("1. Выравнивание по левому краю")
        print("2. Выравнивание по правому краю")
        print("3. Выравнивание по центру")
        print("4. Выравнивание по ширине")
        print("0. Выход из программы")
        try:
            hud_menu = int(input("\nВведите пункт меню: "))
        except ValueError:
            print("\nОшибка: необходимо ввести число!")
            continue
        if hud_menu == 0:
            print("\nВыход из программы.")
            flag = False
        elif hud_menu == 1:
            ex11.text_left_or_right(False)
        elif hud_menu == 2:
            ex11.text_left_or_right(True)
        elif hud_menu == 3:
            ex3.text_center()
        elif hud_menu == 4:
            ex2.text_justifi()
        else:
            print("\nОшибка: неверный пункт меню! Введите число от 0 до 4.")
if __name__ == "__main__":
    main()
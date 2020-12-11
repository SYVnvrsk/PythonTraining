import math


def tasks(chapter, task):
    """Выполнение задачи по номеру главы и номеру задачи"""
    if chapter == 1:
        if task == 1:
            """Вывести на одной строке числа 31, 18 и 79 с одним пробелом между ними"""
            arr = [31, 18, 79]
            for i in range(len(arr)):
                print(arr[i], end=" ")
        elif task == 2:
            """Вывести на одной строке числа 47, 52 и 150 с двумя пробелами между ними"""
            arr = [47, 52, 150]
            for i in range(len(arr)):
                print(arr[i], end="  ")
        elif task == 3:
            """Вывести на экран числа 50 и 10 одно под другим"""
            arr = [50, 10]
            for i in range(len(arr)):
                print(arr[i])
        elif task == 4:
            """Вывести на экран числа 5, 10 и 21 одно под другим"""
            arr = [5, 10, 21]
            for i in range(len(arr)):
                print(arr[i])
        elif task == 5:
            """Получить на экране следующее:
            
            1
            
            2
            
            """
            for i in range(1, 3):
                print()
                print(i)
        elif task == 6:
            """Число пи примерно равно 3,1415926. Вывести на экран это число с тремя цифрами в дробной части"""
            pi = 3.1415926
            print(round(pi, 3))
        elif task == 7:
            """Число е приблизительно равно 2,71828. Вывести на экран это число с точностью до десятых"""
            e = 2.71828
            print(round(e, 1))
        elif task == 8:
            """Составить программу вывода на экран числа, вводимого с клавиатуры. 
            Выводимому числу должно предшествовать сообщение "Вы ввели число" """
            number = input("Введите число: ")
            print("Вы ввели число", number)
        elif task == 9:
            """Составить программу вывода на экран числа, вводимого с клавиатуры. 
            После выводимого числа должно следовать сообщение "- вот какое число Вы ввели" """
            number = input("Введите число: ")
            print(number, "- вот какое число Вы ввели")
        elif task == 10:
            """Составить программу, которая запрашивает имя человека и повторяет его на экране"""
            name = input("Введите имя: ")
            print(name)
        elif task == 11:
            """Составить программу, которая запрашивает название футбольной команды 
            и повторяет его на экране со словами "- это чемпион!" """
            team = input("Введите имя: ")
            print(team, "- это чемпион!")
        elif task == 12:
            """Напишите программу, в которую вводится имя человека и выводится на экран приветствие
            в виде слова "Привет", после которого должна стоять запятая, введённое имя и восклицательный знак.
            После запятой должен стоять пробел, а перед воскл.знаком пробела быть не должно"""
            name = input("Введите имя: ")
            print("Привет, ", name, "!", sep="")
        elif task == 13:
            """Напишите программу, в которое вводится целое число, после чего на экран
            выводится целое и предыдущее целое число"""
            number = int(input("Введите целое число: "))
            print("Следующее за числом", number, "число -", number+1)
            print("Для числа", number, "предыдущее число -", number-1)
        elif task == 14:
            """Составить программу вывода на экран в одну строку трёх любых чисел, вводимых с клавиатуры, 
            с двумя пробелами между ними"""
            number1 = input("Введите число №1: ")
            number2 = input("Введите число №2: ")
            number3 = input("Введите число №3: ")
            print()
            print(number1, number2, number3, sep="  ")
        elif task == 15:
            """Составить программу вывода на экран в одну строку четырёх любых чисел, вводимых с клавиатуры, 
            с одним пробелом между ними"""
            number1 = input("Введите число №1: ")
            number2 = input("Введите число №2: ")
            number3 = input("Введите число №3: ")
            number4 = input("Введите число №4: ")
            print()
            print(number1, number2, number3, number4, sep=" ")
        elif task == 16:
            """Составить программу вывода на экран следующей информации:
                1) 5 10        2) 100 t        3) x 25
                   7 см           1949 v          x y
            """
            choice = input("Введите цифру подзадания (1, 2, 3): ")
            if choice == "1":
                print("5 10")
                print("7 см")
            elif choice == "2":
                t = input("Введите t: ")
                v = input("Введите v: ")
                print("100", t)
                print("1949", v)
            elif choice == "3":
                x = input("Введите x: ")
                y = input("Введите y: ")
                print(x, "25")
                print(x, y)
        elif task == 17:
            """Составить программу вывода на экран следующей информации:
                1) 2 кг         2) a 1         3) x y
                   13 17           19 b           5 y
            """
            choice = input("Введите цифру подзадания (1, 2, 3): ")
            if choice == "1":
                print("2 кг")
                print("13 17")
            elif choice == "2":
                a = input("Введите a: ")
                b = input("Введите b: ")
                print(a, "1")
                print("19", b)
            elif choice == "3":
                x = input("Введите x: ")
                y = input("Введите y: ")
                print(x, y)
                print("5", y)
            else:
                print("There is no subtask with such number in this chapter.")
        else:
            """Тестовый вывод"""
            print("There is no task with such number in this chapter.")
    if chapter == 2:
        if task == 1:
            """Составить программу:
            1) вычисления значения функции y=17x^2-6x+13 при любом значении x
            2) вычисления значения функции y=3a^2+5a-21 при любом значении a"""
            choice = input("Введите номер подзадачи: ")
            if choice == "1":
                x = float(input("Введите x: "))
                y = 17 * (x ** 2) - 6 * x + 13
                print("y =", y)
            elif choice == "2":
                a = float(input("Введите a: "))
                y = 3 * (a ** 2) + 5 * a - 21
                print("y =", y)
            else:
                print("There is no subtask with such number in this chapter.")
        elif task == 2:
            """Составить программу вычисления значения функции (a^2+10)/(sqrt(a^2+1)) при любом значении a"""
            a = float(input("Введите а: "))
            result = (a ** 2 + 10)/(math.sqrt(a ** 2 + 1))
            print("Ответ:", result)
        elif task == 3:
            """Составить программу:
               1) вычисления значения функции sqrt((2a+sin|3a|)/(3,56)) при любом значении а
               2) вычисления значения функции sin((3,2+sqrt(1+x))/(|5x|)) при любом значении х"""
            choice = input("Введите номер подзадачи: ")
            if choice == "1":
                a = float(input("Введите а: "))
                result = math.sqrt((2 * a + math.sin(math.fabs(3 * a)))/3.56)
                print("Ответ:", result)
            elif choice == "2":
                x = float(input("Введите x: "))
                result = math.sin((3.2 + math.sqrt(1 + x))/math.fabs(5 * x))
                print("Ответ:", result)
            else:
                print("There is no subtask with such number in this chapter.")
        elif task == 4:
            """Дана сторона квадрата. Найти его периметр."""
            a = float(input("Введите сторону квадрата: "))
            print("P =", a * 4)
        elif task == 5:
            """Дана радиус окружности. Найти её диаметр."""
            r = float(input("Введите радиус окружности: "))
            print("d =", r / 2)
        else:
            """Тестовый вывод"""
            print("There is no task with such number in this chapter.")
    else:
        """Тестовый вывод"""
        print("You write wrong chapter, fool!")


if __name__ == '__main__':
    chapterNumber = int(input("Введите номер главы: "))
    taskNumber = int(input("Введите номер задачи: "))
    tasks(chapterNumber, taskNumber)

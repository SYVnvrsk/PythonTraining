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
            print("d =", r * 2)
        elif task == 6:
            """Считая, что Земля - идеальная сфера с радиусом R = 6350 км, определить расстояние до линии горизонта
            от точки с заданной высотой над Землёй."""
            r = 6350000
            h = float(input("Введите высоту над землёй (в метрах): "))
            x = math.sqrt(((h + r) ** 2) + (r ** 2))
            print("Расстояние до линии горизонта =", x)
        elif task == 7:
            """Дана длина ребра куба. Найти объём куба и площадь его боковой поверхности."""
            a = float(input("Введите длину ребра куба: "))
            v = a ** 3
            s = 6 * (a ** 2)
            print("v =", v)
            print("s =", s)
        elif task == 8:
            """Дан радиус окружности. Найти длину окружности и площадь круга."""
            r = float(input("Введите радиус окружности: "))
            p = 2 * math.pi * r
            s = math.pi * (r ** 2)
            print("p =", p)
            print("s =", s)
        elif task == 9:
            """Составить программу:
            1) вычисления значения функции z = 2x^3 - 3,44xy + 2,3x^2 - 7,1y +2 при любых значениях х и у
            2) вычисления значения функции x = 3,14(a+b)^3 + 2,75b^2 - 12,7a - 4,1 при любых значениях a и b"""
            choice = input("Введите номер подзадачи: ")
            if choice == "1":
                x = float(input("Введите x: "))
                y = float(input("Введите y: "))
                z = 2 * x ** 3 - 3.44 * x * y + 2.3 * x ** 2 - 7.1 * y + 2
                print("z =", z)
            elif choice == "2":
                a = float(input("Введите a: "))
                b = float(input("Введите b: "))
                x = 3.14 * (a + b) ** 3 + 2.75 * b ** 2 - 12.7 * a - 4.1
                print("x =", x)
            else:
                print("There is no subtask with such number in this chapter.")
        elif task == 10:
            """Даны два числа. Найти:
            а) их среднее арифметическое
            б) их среднее геометрическое"""
            a = float(input("Введите a: "))
            b = float(input("Введите b: "))
            print("Среднее арифметическое =", (a + b) / 2)
            print("Среднее геометрическое =", math.sqrt(a * b))
        elif task == 11:
            """Известны объём и масса тела. Определить плотность материала этого тела."""
            v = float(input("Введите объём тела: "))
            m = float(input("Введите массу тела: "))
            print("Плотность тела =", m / v)
        elif task == 12:
            """Известны количество жителей в государстве и площадь его территории.
            Определить плотность населения в этом государстве."""
            n = float(input("Введите количество жителей: "))
            s = float(input("Введите площадь территории: "))
            print("Плотность населения =", n / s)
        elif task == 13:
            """Составить программу решения линейного уравнения ах+b=0 (a!=0)"""
            a = 0
            while a == 0:
                a = float(input("Введите a, не равное 0: "))
            b = float(input("Введите b: "))
            x = -b / a
            print("x =", x)
        elif task == 14:
            """Даны катеты прямоугольного треугольника. Найти его гипотенузу."""
            a = float(input("Введите катет 1: "))
            b = float(input("Введите катет 2: "))
            c = math.sqrt(a ** 2 + b ** 2)
            print("Гипотенуза =", c)
        elif task == 15:
            """Найти площадь кольца по заданным внешнему и внутреннему радиусам"""
            r1 = float(input("Введите радиус 1: "))
            r2 = float(input("Введите радиус 2: "))
            s1 = math.pi * r1 ** 2
            s2 = math.pi * r2 ** 2
            s = math.fabs(s1 - s2)
            print("Площадь кольца =", s)
        elif task == 16:
            """Даны катеты прямоугольного треугольника. Найти его периметр."""
            a = float(input("Введите катет 1: "))
            b = float(input("Введите катет 2: "))
            print("Периметр =", a + b + math.sqrt(a ** 2 + b ** 2))
        elif task == 17:
            """Даны основания и высота равнобедренной трапеции. Найти её периметр."""
            a = float(input("Введите основание 1: "))
            b = a
            while b == a:
                b = float(input("Введите основание 2: "))
            h = 0
            while h == 0:
                h = float(input("Введите высоту: "))
            if b > a:
                c = math.sqrt(h ** 2 + (b - a / 2) ** 2)
            else:
                c = math.sqrt(h ** 2 + (a - b / 2) ** 2)
            print("Периметр =", a + b + 2 * c)
        elif task == 18:
            """Составить программу вычисления значений функций z и q при любых значениях x и y."""
            x = float(input("Введите x: "))
            y = float(input("Введите y: "))
            z = (x + ((2 + y) / x ** 2))/(y + (1 / (math.sqrt(x ** 2 + 10))))
            q = 7.25 * math.sin(x) - math.fabs(y)
            print("z =", z)
            print("q =", q)
        elif task == 19:
            """Составить программу вычисления значений функций x и y при любых значениях a и b."""
            a = float(input("Введите a: "))
            b = float(input("Введите b: "))
            x = ((2 / (a ** 2 + 25)) + b)/(math.sqrt(b) + ((a + b) / 2))
            y = (math.fabs(a) + 2 * math.sin(b)) / (5.5 * a)
            print("x =", x)
            print("y =", y)
        elif task == 20:
            """Составить программу вычисления значений функций a, b и c при любых значениях e, f, g и h."""
            e = float(input("Введите e: "))
            f = float(input("Введите f: "))
            g = float(input("Введите g: "))
            h = float(input("Введите h: "))
            a = math.sqrt(math.fabs(e - 3 / f) ** 3 + g)
            b = math.sin(e) + math.cos(h) ** 2
            c = (33 * g) / (e * f - 3)
            print("a =", a)
            print("b =", b)
            print("c =", c)
        elif task == 21:
            """Составить программу вычисления значений функций a, b и c при любых значениях e, f, g и h."""
            e = float(input("Введите e: "))
            f = float(input("Введите f: "))
            g = float(input("Введите g: "))
            h = float(input("Введите h: "))
            a = (e + (f / 2)) / 3
            b = math.fabs(h ** 2 - g)
            c = math.sqrt((g - h) ** 2 - 3 * math.sin(e))
            print("a =", a)
            print("b =", b)
            print("c =", c)
        elif task == 22:
            """Даны два числа. Найти среднее арифметическое и среднее геометрическое их модулей."""
            a = float(input("Введите число 1: "))
            b = float(input("Введите число 2: "))
            print("Среднее арифметическое =", (math.fabs(a) + math.fabs(b)) / 2)
            print("Среднее геометрическое =", math.sqrt(math.fabs(a) * math.fabs(b)))
        elif task == 23:
            """Даны стороны прямоугольника. Найти его периметр и длину диагонали."""
            a = float(input("Введите сторону 1: "))
            b = float(input("Введите сторону 2: "))
            p = 2 * (a + b)
            c = math.sqrt(a ** 2 + b ** 2)
            print("p =", p)
            print("c =", c)
        elif task == 24:
            a = float(input("Введите число 1: "))
            b = float(input("Введите число 2: "))
            print("Сумма =", a + b)
            print("Разность =", a - b)
            print("Произведение =", a * b)
            print("Частное =", a / b)
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

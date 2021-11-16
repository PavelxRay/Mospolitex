def f():
    sl = {1: "Первое", 2: "Второе", 3: "Третье", 4: "Четвёртое", 5: "Пятое", 6: "Шестое", 7: "Седьмое",
          8: "Восьмое", 9: "Девятое", 10: "Десятое", 11: "Одиннадцатое", 12: "Двенадцатое", 13: "Тринадцатое",
          14: "Четырнадцатое", 15: "Пятнадцатое", 16: "Шестнадцатое", 17: "Семнадцатое", 18: "Восемнадцатое",
          19: "Девятнадцатое", 20: "Двадцатое", 21: "Двадцатьпервое", 22: "Двадцатьвторое", 23: "Двадцатьтретье",
          24: "Двадцатьчетвёртое", 25: "Двадцатьпятое", 26: "Двадцатьшестое", 27: "Двадцатьседьмое",
          28: "Двадцатьвосьмое", 29: "Двадцатьдевятое", 30: "Тридцатое", 31: "Тридцатьпервое"}
    sl1 = {1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня",
           7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"}
    print("Введите число и месяц(1 - 12) через пробел")
    a, b = map(int, input().split())
    print(f"{sl[a]} {sl1[b]}")
    f_ans()


def f_2():
    print("Введите число:")
    a = int(input())
    if a == 0:
        print("Север")
    elif a > 0:
        if a % 4 == 1:
            print("Запад")
        elif a % 4 == 2:
            print("Юг")
        elif a % 4 == 3:
            print("Восток")
        else:
            print("Север")
    elif a < 0:
        if abs(a) % 4 == 1:
            print("Восток")
        elif abs(a) % 4 == 2:
            print("Юг")
        elif abs(a) % 4 == 3:
            print("Запад")
        else:
            print("Север")
    f_ans()


def f_3():
    t = ""
    sp = ["Десять", "Одиннадцать", "Двенадцать", "Тринадцать",
          "Четырнадцать", "Пятнадцать", "Шестнадцать", "Семнадцать",
          "Восемнадцать", "Девятнадцать"]
    sp1 = ["Двадцать", "Тридцать", "Сорок"]
    sp2 = [" одно", " два", " три", " четыре", " пять", " шесть", " семь", " восемь", " девять"]
    sp3 = [" учебное задание", " учебных заданий", " учебных задания"]
    a = int(input())
    if a < 10 or a > 40:
        print("Кол-во не попадает в диапазон")
    elif 10 <= a < 20:
        t = sp[a - 10] + sp3[1]
    elif a >= 20:
        if not (a % 10):
            t = sp1[(a // 10) - 2] + sp3[1]
        elif a % 10 == 1:
            t = sp1[(a // 10) - 2] + sp2[0] + sp3[0]
        elif 1 < a % 10 < 5:
            t = sp1[(a // 10) - 2] + sp2[a % 10 - 1] + sp3[2]
        elif a % 10 >= 5:
            t = sp1[(a // 10) - 2] + sp2[a % 10 - 1] + sp3[1]
        print(t)
    f_ans()


def f_4():
    t = ""
    sp = ["Сто", "Двести", "Триста", "Четыреста", "Пятьсот", "Шестьсот", "Семьсот", "Восемьсот", "Девятьсот"]
    sp1 = [" двадцать", " тридцать", " сорок", " пятьдесят", " шестьдесят", " семьдесят", " восемьдесят", " девяносто"]
    sp2 = [" один", " два", " три", " четыре", " пять", " шесть", " семь", " восемь", " девять"]
    sp3 = [" десять", " одиннадцать", " двенадцать", " тринадцать",
           " четырнадцать", " пятнадцать", " шестнадцать", " семнадцать",
           " восемнадцать", " девятнадцать"]
    print("Введите число от 100 до 999")
    a = int(input())
    if a < 100 or a > 999:
        print("Число не попадает в диапазон")
    elif 0 < a % 100 < 10:
        print(sp[(a // 100) - 1] + sp2[(a % 10) - 1])
    elif 10 < a % 100 < 20:
        print(sp[(a // 100) - 1] + sp3[(a % 100) - 10])
    elif a % 100 >= 20 and a % 10 == 0:
        print(sp[(a // 100) - 1] + sp1[((a % 100) // 10) - 2])
    elif a % 100 >= 20 and a % 10 > 0:
        print(sp[(a // 100) - 1] + sp1[((a % 100) // 10) - 2] + sp2[(a % 10) - 1])
    f_ans()


def f_5():
    sp = ["зелёной", "красной", "жёлтой", "белой", "чёрной"]
    sp1 = ["зелёного", "красного", "жёлтого", "белого", "чёрного"]
    zh1 = ["крысы", "коровы", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]
    zh2 = ["тигра", "зайца", "дракрна"]
    print("Введите год")
    a = int(input())
    if (a - 1984) < 0:
        while (a - 1984) < -60:
            a += 60
    if (a - 1984) % 60 <= 11:
        if (a - 1984) % 12 == 0:
            print(f"Год {sp[0]} {zh1[0]}")
        elif (a - 1984) % 12 == 1:
            print(f"Год {sp[0]} {zh1[1]}")
        elif (a - 1984) % 12 == 2:
            print(f"Год {sp1[0]} {zh2[0]}")
        elif (a - 1984) % 12 == 3:
            print(f"Год {sp1[0]} {zh2[1]}")
        elif (a - 1984) % 12 == 4:
            print(f"Год {sp1[0]} {zh2[2]}")
        elif (a - 1984) % 12 == 5:
            print(f"Год {sp[0]} {zh1[2]}")
        elif (a - 1984) % 12 == 6:
            print(f"Год {sp[0]} {zh1[3]}")
        elif (a - 1984) % 12 == 7:
            print(f"Год {sp[0]} {zh1[4]}")
        elif (a - 1984) % 12 == 8:
            print(f"Год {sp[0]} {zh1[5]}")
        elif (a - 1984) % 12 == 9:
            print(f"Год {sp[0]} {zh1[6]}")
        elif (a - 1984) % 12 == 10:
            print(f"Год {sp[0]} {zh1[7]}")
        elif (a - 1984) % 12 == 11:
            print(f"Год {sp[0]} {zh1[8]}")
    elif 23 >= (a - 1984) % 60 > 11:
        if (a - 1984) % 12 == 0:
            print(f"Год {sp[1]} {zh1[0]}")
        elif (a - 1984) % 12 == 1:
            print(f"Год {sp[1]} {zh1[1]}")
        elif (a - 1984) % 12 == 2:
            print(f"Год {sp1[1]} {zh2[0]}")
        elif (a - 1984) % 12 == 3:
            print(f"Год {sp1[1]} {zh2[1]}")
        elif (a - 1984) % 12 == 4:
            print(f"Год {sp1[1]} {zh2[2]}")
        elif (a - 1984) % 12 == 5:
            print(f"Год {sp[1]} {zh1[2]}")
        elif (a - 1984) % 12 == 6:
            print(f"Год {sp[1]} {zh1[3]}")
        elif (a - 1984) % 12 == 7:
            print(f"Год {sp[1]} {zh1[4]}")
        elif (a - 1984) % 12 == 8:
            print(f"Год {sp[1]} {zh1[5]}")
        elif (a - 1984) % 12 == 9:
            print(f"Год {sp[1]} {zh1[6]}")
        elif (a - 1984) % 12 == 10:
            print(f"Год {sp[1]} {zh1[7]}")
        elif (a - 1984) % 12 == 11:
            print(f"Год {sp[1]} {zh1[8]}")
    elif 35 >= (a - 1984) % 60 > 23:
        if (a - 1984) % 12 == 0:
            print(f"Год {sp[2]} {zh1[0]}")
        elif (a - 1984) % 12 == 1:
            print(f"Год {sp[2]} {zh1[1]}")
        elif (a - 1984) % 12 == 2:
            print(f"Год {sp1[2]} {zh2[0]}")
        elif (a - 1984) % 12 == 3:
            print(f"Год {sp1[2]} {zh2[1]}")
        elif (a - 1984) % 12 == 4:
            print(f"Год {sp1[2]} {zh2[2]}")
        elif (a - 1984) % 12 == 5:
            print(f"Год {sp[2]} {zh1[2]}")
        elif (a - 1984) % 12 == 6:
            print(f"Год {sp[2]} {zh1[3]}")
        elif (a - 1984) % 12 == 7:
            print(f"Год {sp[2]} {zh1[4]}")
        elif (a - 1984) % 12 == 8:
            print(f"Год {sp[2]} {zh1[5]}")
        elif (a - 1984) % 12 == 9:
            print(f"Год {sp[2]} {zh1[6]}")
        elif (a - 1984) % 12 == 10:
            print(f"Год {sp[2]} {zh1[7]}")
        elif (a - 1984) % 12 == 11:
            print(f"Год {sp[2]} {zh1[8]}")
    elif 47 >= (a - 1984) % 60 > 35:
        if (a - 1984) % 12 == 0:
            print(f"Год {sp[3]} {zh1[0]}")
        elif (a - 1984) % 12 == 1:
            print(f"Год {sp[3]} {zh1[1]}")
        elif (a - 1984) % 12 == 2:
            print(f"Год {sp1[3]} {zh2[0]}")
        elif (a - 1984) % 12 == 3:
            print(f"Год {sp1[3]} {zh2[1]}")
        elif (a - 1984) % 12 == 4:
            print(f"Год {sp1[3]} {zh2[2]}")
        elif (a - 1984) % 12 == 5:
            print(f"Год {sp[3]} {zh1[2]}")
        elif (a - 1984) % 12 == 6:
            print(f"Год {sp[3]} {zh1[3]}")
        elif (a - 1984) % 12 == 7:
            print(f"Год {sp[3]} {zh1[4]}")
        elif (a - 1984) % 12 == 8:
            print(f"Год {sp[3]} {zh1[5]}")
        elif (a - 1984) % 12 == 9:
            print(f"Год {sp[3]} {zh1[6]}")
        elif (a - 1984) % 12 == 10:
            print(f"Год {sp[3]} {zh1[7]}")
        elif (a - 1984) % 12 == 11:
            print(f"Год {sp[3]} {zh1[8]}")
    elif 59 >= (a - 1984) % 60 > 47:
        if (a - 1984) % 12 == 0:
            print(f"Год {sp[4]} {zh1[0]}")
        elif (a - 1984) % 12 == 1:
            print(f"Год {sp[4]} {zh1[1]}")
        elif (a - 1984) % 12 == 2:
            print(f"Год {sp1[4]} {zh2[0]}")
        elif (a - 1984) % 12 == 3:
            print(f"Год {sp1[4]} {zh2[1]}")
        elif (a - 1984) % 12 == 4:
            print(f"Год {sp1[4]} {zh2[2]}")
        elif (a - 1984) % 12 == 5:
            print(f"Год {sp[4]} {zh1[2]}")
        elif (a - 1984) % 12 == 6:
            print(f"Год {sp[4]} {zh1[3]}")
        elif (a - 1984) % 12 == 7:
            print(f"Год {sp[4]} {zh1[4]}")
        elif (a - 1984) % 12 == 8:
            print(f"Год {sp[4]} {zh1[5]}")
        elif (a - 1984) % 12 == 9:
            print(f"Год {sp[4]} {zh1[6]}")
        elif (a - 1984) % 12 == 10:
            print(f"Год {sp[4]} {zh1[7]}")
        elif (a - 1984) % 12 == 11:
            print(f"Год {sp[4]} {zh1[8]}")
    f_ans()


def f_ans():
    print("Выберите номер задания от 1 до 5:")
    print("Для завершения программы введите 0")
    ans = int(input())
    if ans == 0:
        print("Конец программы.")

    elif ans == 1:
        f()
    elif ans == 2:
        f_2()
    elif ans == 3:
        f_3()
    elif ans == 4:
        f_4()
    elif ans == 5:
        f_5()
    else:
        print("Error, try again")
        f_ans()


f_ans()
def f():
    print("Введите число A:")
    a = int(input())
    print("Введите число B:")
    b = int(input())
    c = max(a, b)
    if a != b:
        a, b = c, c
    else:
        a, b = 0, 0
    print(f"A = {a}, B = {b}")
    f_ans()


def f_2():
    print("Введите число A:")
    a = int(input())
    print("Введите число B:")
    b = int(input())
    print("Введите число C:")
    c = int(input())
    d = min(a, b, c)
    print(f"Сумма наибольших двух чисел = {a + b + c - d}")
    f_ans()


def f_3():
    print("Введите число A:")
    a = input().split(",")
    print("Введите число B:")
    b = input().split(",")
    print("Введите число C:")
    c = input().split(",")
    res1 = ((int(a[0]) - int(b[0])) ** 2 + (int(a[1]) - int(b[1])) ** 2) ** 0.5
    res2 = ((int(a[0]) - int(c[0])) ** 2 + (int(a[1]) - int(c[1])) ** 2) ** 0.5
    if res1 < res2:
        print(f"Расстояние от точки B: {res1}")
    else:
        print(f"Расстояние от точки C: {res2}")
    f_ans()


def f_4():
    print("Введите точку:")
    x, y = map(int, input().split(","))
    if x > 0 and y > 0:
        print(f"Точка лежит в первой четверти.")
    elif x > 0 and y < 0:
        print(f"Точка лежит в четвёртой четверти.")
    elif x < 0 and y > 0:
        print(f"Точка лежит в второй четверти.")
    elif x < 0 and y < 0:
        print(f"Точка лежит в третьей четверти.")
    f_ans()


def f_5():
    res1 = "Положительное число"
    res2 = "Отрицательное число"
    res3 = "Чётное"
    res4 = "Нечётное"
    print("Введите число:")
    a = int(input())
    if a == 0:
        print("Нулевое")
    else:
        if a > 0 and a % 2:
            print(f"{res1} {res4}")
        elif a > 0 and not (a % 2):
            print(f"{res1} {res3}")
        elif a < 0 and not (a % 2):
            print(f"{res2} {res3}")
        elif a < 0 and a % 2:
            print(f"{res2} {res4}")
    f_ans()


def f_6():
    res1 = "двузначное число"
    res2 = "трёхзначное число"
    rr = "однозначное число"
    res3 = "Чётное"
    res4 = "Нечётное"
    print("Введите число:")
    a = int(input())
    if 0 < a < 10 and a % 2:
        print(f"{res4} {rr}")
    elif 0 < a < 10 and not (a % 2):
        print(f"{res3} {rr}")
    elif 9 < a < 100 and not (a % 2):
        print(f"{res3} {res1}")
    elif 9 < a < 100 and a % 2:
        print(f"{res4} {res1}")
    elif 99 < a < 1000 and not (a % 2):
        print(f"{res3} {res2}")
    elif 99 < a < 1000 and a % 2:
        print(f"{res4} {res2}")
    f_ans()


def f_ans():
    print("Выберите номер задания от 1 до 6:")
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
    elif ans == 6:
        f_6()
    else:
        print("Error, try again")
        f_ans()


f_ans()

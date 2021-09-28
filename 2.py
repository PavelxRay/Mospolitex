print("Выберите номер задания от 1 до 7:")


def f():
    print("Введите две переменные:")
    sp = input().split()
    a, b = sp[0], sp[1]
    a, b = b, a
    print(a, b)


def f_2():
    print("Введите три переменные:")
    sp = input().split()
    a, b, c = sp[0], sp[1], sp[2]
    a, b, c = b, c, a
    print(a, b, c)


def f_3():
    print("Введите три переменные:")
    sp = input().split()
    a, b, c = sp[0], sp[1], sp[2]
    a, b, c = c, a, b
    print(a, b, c)


def f_4():
    print("Введите число:")
    x = int(input())
    print(3 * x ** 6 - 6 * x ** 2 - 7)


def f_5():
    print("Введите число:")
    x = int(input())
    print(4 * (x - 3) ** 6 - 7 * (x - 3) ** 3 + 2)


def f_6():
    print("Введите число:")
    a = int(input())
    b = a * a
    b *= b
    print(b * b)


def f_7():
    print("Введите число:")
    a = int(input())
    a = a * a
    b = a ** 0.5 * a
    c = a * b
    a = c * c
    print(a * c)


def f_ans():
    ans = int(input())
    if ans == 1:
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
    elif ans == 7:
        f_7()
    else:
        print("Error, try again")
        f_ans()


f_ans()

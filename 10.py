def f():
    print("Введите число A:")
    a = int(input())
    print("Введите число B:")
    b = int(input())
    if a > 2 and b <= 3:
        print(True)
    else:
        print(False)
    f_ans()


def f_2():
    print("Введите число A:")
    a = int(input())
    print("Введите число B:")
    b = int(input())
    print("Введите число C:")
    c = int(input())
    if a < b < c:
        print(True)
    else:
        print(False)
    f_ans()


def f_3():
    print("Введите число:")
    a = input()
    if len(a) == 2:
        print(True)
    else:
        print(False)
    f_ans()


def f_4():
    print("Введите трехзначное число:")
    num = int(input())
    x = [int(a) for a in str(num)]
    if int(x[0]) > int(x[1]) > int(x[2]) or int(x[0]) < int(x[1]) < int(x[2]):
        print(True)
    else:
        print(False)
    f_ans()


def f_5():
    print("Введите четырёхзначное число:")
    num = int(input())
    x = [int(a) for a in str(num)]
    if x == x[::-1]:
        print(True)
    else:
        print(False)

    f_ans()


def f_6():
    print("Введите сторону A:")
    a = int(input())
    print("Введите сторону B:")
    b = int(input())
    print("Введите сторону C:")
    c = int(input())
    if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 \
            or c ** 2 + b ** 2 == a ** 2:
        print(True)
    else:
        print(False)
    f_ans()


def f_7():
    print("Введите сторону A:")
    a = int(input())
    print("Введите сторону B:")
    b = int(input())
    print("Введите сторону C:")
    c = int(input())
    sp = sorted([a, b, c])
    if sp[0] + sp[1] > sp[2]:
        print(True)
    else:
        print(False)
    f_ans()


def f_ans():
    print("Выберите номер задания от 1 до 7:")
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
    elif ans == 7:
        f_7()
    else:
        print("Error, try again")
        f_ans()


f_ans()

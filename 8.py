def f():
    print("Введите размер файла в байтах")
    a = int(input())
    print(f"Размер файла в Килобайтах: {int(a / 1024)}")
    f_ans()


def f_2():
    print("Введите значение отрезка A:")
    a = int(input())
    print("Введите значение отрезка B, (A > B):")
    b = int(input())
    print(f"В отрезок A помещается {int(a / b)} отрезков B")
    f_ans()


def f_3():
    print("Введите значение отрезка A:")
    a = int(input())
    print("Введите значение отрезка B, (A > B):")
    b = int(input())
    print(f"При наложении максимльно возможных отрезков B, незанятая часть A равна: {a - (b * int(a / b))}")
    f_ans()


def f_4():
    print("Введите двузначное число которое хотите отразить:")
    num = int(input())
    x = [int(a) for a in str(num)]
    print(f"{x[-1]}{x[0]}")
    f_ans()


def f_5():
    print("Введите трехзначное число:")
    num = int(input())
    x = [int(a) for a in str(num)]
    print(f"{x[1]}{x[2]}{x[0]}")


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

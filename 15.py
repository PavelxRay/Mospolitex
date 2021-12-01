import math


def PowerA3(a, b):
    b += a ** 3
    return b


def Sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    return 1


def RingS(a, b):
    sp = sorted([a, b])
    return math.pi * (sp[-1] ** 2 - sp[0] ** 2)


def Quarter(a):
    x, y = map(int, a.split(", "))
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3


def Fact2(a):
    ans = 1
    if a % 2:
        for i in range(1, a + 1, 2):
            ans *= i
        return ans
    else:
        for i in range(2, a + 1, 2):
            ans *= i
        return ans


def f_ans():
    print("Выберите номер задания от 1 до 5:")
    print("Для завершения программы введите 0")
    ans = int(input())
    if ans == 0:
        print("Конец программы.")
    elif ans == 1:
        for i in range(5):
            print("Введите число:")
            a = int(input())
            b = 0
            print(PowerA3(a, b))
        f_ans()
    elif ans == 2:
        print("Введите число:")
        x = int(input())
        print("Введите число:")
        x1 = int(input())
        a = Sign(x) + Sign(x1)
        print(a)
        f_ans()
    elif ans == 3:
        print("Введите число:")
        r1 = int(input())
        print("Введите число:")
        r2 = int(input())
        print(RingS(r1, r2))
        f_ans()
    elif ans == 4:
        for i in range(3):
            print("Введите точку через заяпятую с пробелом")  # Да, работает чуть подругому но по моему так круче,
            # нежели по одному числу вводить
            a = input()
            print(Quarter(a))
        f_ans()
    elif ans == 5:
        print("Введите число:")
        n = int(input())
        print(Fact2(n))
        f_ans()
    else:
        print("Error, try again")
        f_ans()


f_ans()

def f():
    print("Введите стоимость за 1 кг. в рублях")
    a = float(input())
    b = 0.1
    for i in range(10):
        print(f"Цена за {b} кг {b * a} руб.")
        b += 0.1
    f_ans()


def f_2():
    print("Введите число:")
    a = int(input())
    b = 0.1
    c = 1
    d = 1
    for i in range(a):
        c *= (d + b)
        d += b
    print(c)
    f_ans()


def f_3():
    print("Введите число")
    a = int(input())
    ans = 0
    for i in range(1, 2 * a, 2):
        if i == (2 * a) - 1:
            print(f"Квадрат числа = {ans + i}")
        else:
            print(ans + i)
            ans += i
    f_ans()


def f_4():
    print("Введите число")
    a = int(input())
    print("Введите степень")
    b = int(input())
    ans = 0
    for i in range(b + 1):
        ans += a ** i
    print(ans)
    f_ans()


def f_5():
    print("Введите число")
    a = int(input())
    print("Введите степень")
    b = int(input())
    ans, r = 1, 1
    for i in range(b):
        r *= -a
        ans += r
    print(ans)
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
